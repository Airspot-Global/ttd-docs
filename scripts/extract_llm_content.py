"""Convert the <article id="llm-content"> block of a saved OpenTTD page to Markdown.

usage: python3 -I scripts/extract_llm_content.py <page-file> <page-url>
Standard library only. Exit codes: 2 = no llm-content article, 3 = unbalanced table markup.
"""

import re
import sys
from html.parser import HTMLParser
from urllib.parse import urljoin

BLOCK = {"p", "div", "section", "article", "header", "footer", "figure", "figcaption", "dl", "dt", "dd"}
SKIP = {"script", "style", "svg", "button", "nav"}


class Unbalanced(Exception):
    pass


class Md(HTMLParser):
    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base = base
        self.out = []
        self.lists = []
        self.pre = 0
        self.skip = 0
        self.links = []
        self.tables = []
        self.quotes = []

    def open_cell(self):
        for t in reversed(self.tables):
            if t["cell"] is not None:
                return t["cell"]
        return None

    def emit(self, s):
        cell = self.open_cell()
        if cell is not None:
            cell.append(s)
        else:
            self.out.append(s)

    def newline(self, n=1):
        cell = self.open_cell()
        if cell is not None:
            cell.append(" ")
            return
        self.out.append("\n" * n)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.skip or tag in SKIP:
            if tag in SKIP:
                self.skip += 1
            return
        if self.pre:
            return
        if re.fullmatch(r"h[1-6]", tag):
            self.newline(2)
            self.emit("#" * int(tag[1]) + " ")
        elif tag in BLOCK:
            self.newline(2)
        elif tag == "br":
            self.newline()
        elif tag in ("ul", "ol"):
            self.lists.append([tag, 0])
            self.newline()
        elif tag == "li":
            self.newline()
            depth = max(len(self.lists) - 1, 0)
            if self.lists and self.lists[-1][0] == "ol":
                self.lists[-1][1] += 1
                self.emit("   " * depth + f"{self.lists[-1][1]}. ")
            else:
                self.emit("  " * depth + "- ")
        elif tag == "pre":
            self.newline(2)
            self.emit("```\n")
            self.pre += 1
        elif tag == "code":
            self.emit("`")
        elif tag in ("strong", "b"):
            self.emit("**")
        elif tag in ("em", "i"):
            self.emit("_")
        elif tag == "blockquote":
            self.quotes.append(self.out)
            self.out = []
        elif tag == "a":
            href = a.get("href") or ""
            self.links.append(href)
            if href:
                self.emit("[")
        elif tag == "img":
            alt = a.get("alt") or ""
            if alt:
                self.emit(f"[image: {alt}]")
        elif tag == "table":
            self.newline(2)
            self.tables.append({"rows": [], "cell": None})
        elif tag == "tr" and self.tables:
            self.tables[-1]["rows"].append([])
        elif tag in ("td", "th") and self.tables:
            self.tables[-1]["cell"] = []

    def handle_endtag(self, tag):
        if tag in SKIP:
            if self.skip:
                self.skip -= 1
            return
        if self.skip:
            return
        if tag == "pre":
            self.pre = max(self.pre - 1, 0)
            if not "".join(self.out).endswith("\n"):
                self.emit("\n")
            self.emit("```")
            self.newline(2)
            return
        if self.pre:
            return
        if re.fullmatch(r"h[1-6]", tag) or tag in BLOCK:
            self.newline(2)
        elif tag in ("ul", "ol"):
            if self.lists:
                self.lists.pop()
            self.newline()
        elif tag == "code":
            self.emit("`")
        elif tag in ("strong", "b"):
            self.emit("**")
        elif tag in ("em", "i"):
            self.emit("_")
        elif tag == "blockquote" and self.quotes:
            inner = tidy("".join(self.out))
            self.out = self.quotes.pop()
            self.newline(2)
            self.emit("\n".join(("> " + ln).rstrip() for ln in inner.split("\n")))
            self.newline(2)
        elif tag == "a":
            href = self.links.pop() if self.links else ""
            if href:
                self.emit(f"]({urljoin(self.base, href)})")
        elif tag in ("td", "th"):
            if not self.tables:
                raise Unbalanced(f"</{tag}> with no open table")
            t = self.tables[-1]
            if t["cell"] is not None:
                text = re.sub(r"\s+", " ", "".join(t["cell"])).strip()
                if t["rows"]:
                    t["rows"][-1].append(text)
                t["cell"] = None
        elif tag == "table":
            if not self.tables:
                raise Unbalanced("</table> with no open table")
            rows = [r for r in self.tables.pop()["rows"] if r]
            outer = self.open_cell()
            if outer is not None:
                # Nested table: flatten into the open outer cell. Its cell text is already escaped, so it is
                # appended directly (not through emit/handle_data) and must not be escaped again.
                if rows:
                    outer.append(" " + "<br>".join(" · ".join(r) for r in rows) + " ")
                return
            if rows:
                width = max(len(r) for r in rows)
                rows = [r + [""] * (width - len(r)) for r in rows]
                lines = ["| " + " | ".join(rows[0]) + " |", "|" + " --- |" * width]
                lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
                self.emit("\n".join(lines))
            self.newline(2)

    def handle_data(self, data):
        if self.skip:
            return
        if self.pre:
            self.emit(data)
            return
        if not data.strip() and "\n" in data:
            return
        text = re.sub(r"\s+", " ", data)
        if self.open_cell() is not None:
            text = text.replace("|", "\\|")
        self.emit(text)


def tidy(text):
    text = "\n".join(ln.rstrip() for ln in text.split("\n"))
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return re.sub(r"(?m)^(#{1,6}) +", r"\1 ", text)


def main():
    page, url = sys.argv[1], sys.argv[2]
    src = open(page, encoding="utf-8", errors="replace").read()
    m = re.search(r'<article id="llm-content"[^>]*>(.*?)</article>', src, re.S)
    if not m or not m.group(1).strip():
        print(f"no llm-content article in {page}", file=sys.stderr)
        sys.exit(2)
    p = Md(url)
    try:
        p.feed(m.group(1))
        p.close()
        if p.tables:
            raise Unbalanced(f"{len(p.tables)} table(s) still open at the end of the article")
    except Unbalanced as e:
        print(f"unbalanced table in {page}: {e}", file=sys.stderr)
        sys.exit(3)
    print(tidy("".join(p.out)))


if __name__ == "__main__":
    main()
