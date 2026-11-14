"""Merge freshly extracted OpenTTD pages into the repo, driven by manifest.tsv.

usage: python3 -I scripts/merge_docs.py <repo-root> <out-dir> <retrieved-date> [--write]
  <out-dir> is the folder refresh-docs.sh wrote (md/ and _sitemap_urls.txt).
  Without --write it only prints the summary (dry run).

For each manifest row it keeps the Airspot blocks of the current file
(<!-- airspot:begin ... --> ... <!-- airspot:end -->), writes the new header and body,
puts the blocks back (README rule 3), and updates sha256/retrieved. Nothing is written
if any row fails.
"""
import hashlib
import os
import re
import sys
from urllib.parse import unquote

HOST = "https://open.thetradedesk.com"
COLS = ["local_path", "live_url", "legacy_url", "retrieved", "status", "sha256"]
BLOCK_RE = re.compile(r'<!-- airspot:begin (anchor|placement)="([^"]*)" -->\n.*?\n<!-- airspot:end -->', re.S)
OLD_ENTRY_RE = re.compile(r"^(get|post|put|delete|patch|gql)\[(.+?)\]\((/v3/portal/[^)]+)\)(legacy|deprecated)?\s*$")
PORTAL_LINK_RE = re.compile(r"\]\((?:https://partner\.thetradedesk\.com)?(/v3/portal/[^)\s]+)\)")
BANNER = "> **Removed from TTD docs (checked {date}).**"


def page_name(url):
    return re.sub(r"[?#].*", "", url.split("/docsApp/", 1)[1]).replace("/", "__")


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_manifest(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        header = f.readline().rstrip("\n").split("\t")
        assert header == COLS, header
        for line in f:
            if line.strip():
                rows.append(dict(zip(COLS, line.rstrip("\n").split("\t"))))
    return rows


def write_manifest(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\t".join(COLS) + "\n")
        for r in sorted(rows, key=lambda r: r["local_path"]):
            f.write("\t".join(r[c] for c in COLS) + "\n")


class Links:
    """Maps retired /v3/portal/... links to OpenTTD URLs found in the sitemap."""

    def __init__(self, sitemap_urls):
        self.by_key = {}
        for u in sitemap_urls:
            if "/advertiser/docsApp/" not in u:
                continue
            parts = u.split("/docsApp/", 1)[1].split("/")
            if len(parts) == 4:
                key = (parts[2], unquote(parts[3]).lower())
                self.by_key.setdefault(key, u)
        self.unknown = set()

    def resolve(self, link):
        path, _, frag = link.partition("#")
        parts = path.split("/")
        if len(parts) < 6:
            return None
        kind, name = parts[4], unquote(parts[5]).lower()
        url = self.by_key.get((kind, name))
        if not url:
            return None
        return url + ("#" + frag if frag else "")

    def rewrite(self, text, where):
        def sub(m):
            new = self.resolve(m.group(1))
            if new:
                return "](" + new + ")"
            self.unknown.add((where, m.group(1)))
            return m.group(0)

        return PORTAL_LINK_RE.sub(sub, text)


def split_file(text):
    """Return (header_lines, body) of a repo file. The header ends at the first '---' line."""
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        if ln.strip() == "---":
            return lines[:i], "\n".join(lines[i + 1:])
    return lines, ""


def take_blocks(text):
    blocks = [(m.group(1), m.group(2), m.group(0)) for m in BLOCK_RE.finditer(text)]
    text = BLOCK_RE.sub("\x00", text)
    text = re.sub(r"\n*\x00\n*", "\n\n", text)
    return blocks, text


def heading_text(line):
    m = re.match(r"^#{1,6}\s+(.*)$", line)
    if not m:
        return None
    return re.sub(r"\[\]\(#[^)]*\)\s*$", "", m.group(1)).strip().lower()


def insert_anchor(body, anchor, block):
    lines = body.split("\n")
    fence = False
    for i, ln in enumerate(lines):
        if ln.startswith("```"):
            fence = not fence
            continue
        if not fence and heading_text(ln) == anchor.strip().lower():
            rest = "\n".join(lines[i + 1:]).lstrip("\n")
            return "\n".join(lines[: i + 1]) + "\n\n" + block + ("\n\n" + rest if rest else ""), True
    return body, False


def convert_area(old_body, sitemap, links, where):
    """Old portal area page -> endpoint list with one heading per operation."""
    lines = old_body.split("\n")
    start = next((i for i, ln in enumerate(lines) if OLD_ENTRY_RE.match(ln)), None)
    if start is None:
        return old_body.strip("\n"), []
    out, gone = ["## Operations and endpoints", ""], []
    i = start
    while i < len(lines):
        m = OLD_ENTRY_RE.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        verb, label, link, legacy = m.groups()
        slug = link.rstrip("/").split("/")[-1]
        kind = link.split("/")[4]
        live = f"{HOST}/advertiser/docsApp/AdvertiserReferences/api/{kind}/{slug}"
        title = f"GraphQL {label}" if verb == "gql" else f"{verb.upper()} {label}"
        out.append(f"### {title}{f' ({legacy})' if legacy else ''}")
        out.append("")
        if live in sitemap:
            out.append(f"Reference: {live}")
        else:
            out.append(f"Reference: not in TTD's live reference (old link `{link}`).")
            gone.append(live)
        i += 1
    body = links.rewrite("\n".join(out).strip("\n"), where)
    return re.sub(r"\n{3,}", "\n\n", body), gone


def main():
    root, out, date = sys.argv[1], sys.argv[2], sys.argv[3]
    write = "--write" in sys.argv[4:]
    sitemap_list = [u.strip() for u in open(os.path.join(out, "_sitemap_urls.txt"), encoding="utf-8") if u.strip()]
    sitemap = set(sitemap_list)
    links = Links(sitemap_list)
    mpath = os.path.join(root, "manifest.tsv")
    rows = read_manifest(mpath)
    for r in rows:
        if r["status"] == "renamed" and r["legacy_url"]:
            links.by_key[("doc", unquote(r["legacy_url"].rsplit("/", 1)[-1]).lower())] = r["live_url"]
    results, errors, warnings = {}, [], []
    summary = {"changed": [], "unchanged": [], "new": [], "removed": []}

    for r in rows:
        path = os.path.join(root, r["local_path"])
        exists = os.path.exists(path)
        current = open(path, encoding="utf-8").read() if exists else ""
        blocks, current_clean = take_blocks(current)
        head, cur_body = split_file(current_clean)
        title = head[0][2:].strip() if head and head[0].startswith("# ") else None
        category = r["local_path"].split("/")[0]
        legacy = r["legacy_url"]
        status = r["status"]
        url = r["live_url"]
        note = ""

        if status == "removed":
            body = links.rewrite(cur_body.strip("\n"), r["local_path"])
            if not body.startswith("> **Removed from TTD docs"):
                nearest = r["live_url"] or "none"
                body = (BANNER.format(date=date) + " This page is no longer on TTD's documentation site. "
                        "The text below is the pre-refresh copy, kept because Airspot code or notes may cite it. "
                        f"Nearest live page: {nearest}\n\n" + body)
            source = "removed from TTD docs" + (f" (nearest live page: {url})" if url else "")
            note = " (removal checked; body is the pre-refresh copy)"
        elif "/api/area/" in url:
            body, gone = convert_area(cur_body, sitemap, links, r["local_path"])
            if gone:
                warnings.append(f"{r['local_path']}: not in live reference: {', '.join(gone)}")
            source = url
            note = (" (endpoint list from the pre-refresh copy; the live area page is drawn in the browser,"
                    " so only its endpoint links were checked against the sitemap)")
        else:
            md = os.path.join(out, "md", page_name(url) + ".md")
            if not os.path.exists(md):
                errors.append(f"{r['local_path']}: no extracted text for {url}")
                continue
            body = open(md, encoding="utf-8").read().strip("\n")
            if title is None:
                m = re.match(r"^# (.+)$", body.split("\n", 1)[0])
                title = m.group(1).strip() if m else page_name(url).split("__")[-1]
            source = url
        if title is None:
            errors.append(f"{r['local_path']}: no title")
            continue

        digest = sha(body)
        if exists and digest == r["sha256"] and "\n- Retrieved:" in current:
            summary["unchanged"].append(r["local_path"])
            continue

        header = [f"# {title}", "", f"- Source: {source}"]
        if legacy:
            header.append(f"- Legacy source: {legacy} (retired)")
        header.append(f"- Retrieved: {date}{note}")
        header.append(f"- Category: {category}")
        after = []
        for mode, value, text in blocks:
            if mode == "placement" and value == "header":
                header.append(text)
            elif mode == "placement" and value == "after-header":
                after.append(text)
        text = "\n".join(header) + "\n\n---\n\n"
        if after:
            text += "\n\n".join(after) + "\n\n"
        missing = []
        for mode, value, block in blocks:
            if mode != "anchor":
                continue
            body, ok = insert_anchor(body, value, block)
            if not ok:
                missing.append(block)
                warnings.append(f"{r['local_path']}: anchor not found: {value}")
        if missing:
            body += "\n\n## Airspot notes (anchor not found)\n\n" + "\n\n".join(missing)
        results[path] = text + body + "\n"
        r["sha256"] = digest
        r["retrieved"] = date
        key = "removed" if status == "removed" else ("changed" if exists else "new")
        summary[key].append(r["local_path"])

    for k, v in summary.items():
        print(f"{k}: {len(v)}")
    for w in warnings:
        print("WARN", w)
    for where, link in sorted(links.unknown):
        print("UNMAPPED-LINK", where, link)
    if errors:
        for e in errors:
            print("ERROR", e)
        sys.exit("nothing written")
    if write:
        for path, text in results.items():
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
        write_manifest(mpath, rows)
        print(f"written: {len(results)}")


if __name__ == "__main__":
    main()
