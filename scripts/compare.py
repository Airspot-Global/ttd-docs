import re, sys, os, difflib
local_root, live_dir, adv_urls = sys.argv[1], sys.argv[2], sys.argv[3]
def norm(t):
    t = re.sub(r'\]\([^)]*\)', ']', t)          # drop link targets
    t = re.sub(r'\[\]\(#[^)]*\)', '', t)
    t = re.sub(r'[`*_>#\[\]|]', ' ', t)
    t = t.lower()
    return re.findall(r'[a-z0-9]+', t)
rows = []
for sub in ("GraphQL", "Guides"):
    for fn in sorted(os.listdir(os.path.join(local_root, sub))):
        p = os.path.join(local_root, sub, fn)
        txt = open(p, encoding="utf-8").read()
        m = re.search(r'^- Source: (\S+)', txt, re.M)
        if not m: continue
        name = m.group(1).rsplit("/", 1)[-1]
        cands = [f for f in os.listdir(live_dir) if f.endswith("__" + name + ".md")]
        if not cands:
            rows.append((sub + "/" + fn, name, "-", "-", "-")); continue
        live = open(os.path.join(live_dir, cands[0]), encoding="utf-8").read()
        body = txt.split("\n---\n", 1)[-1]
        a, b = norm(body), norm(live)
        r = difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()
        rows.append((sub + "/" + fn, name, len(a), len(b), "%.2f" % r))
for r in rows: print("\t".join(map(str, r)))
