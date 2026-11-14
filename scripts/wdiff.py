import re, sys, difflib
loc, live = sys.argv[1], sys.argv[2]
maxn = int(sys.argv[3]) if len(sys.argv) > 3 else 40
def toks(t):
    t = re.sub(r'\]\([^)]*\)', ']', t); t = re.sub(r'\[\]\(#[^)]*\)', '', t)
    t = re.sub(r'[`*_>#\[\]|]', ' ', t)
    return t.split()
a = toks(open(loc, encoding="utf-8").read().split("\n---\n", 1)[-1]); b = toks(open(live, encoding="utf-8").read())
sm = difflib.SequenceMatcher(None, [x.lower() for x in a], [x.lower() for x in b], autojunk=False)
n = 0
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == "equal": continue
    old, new = " ".join(a[i1:i2]), " ".join(b[j1:j2])
    if len(old) + len(new) < 4: continue
    ctx = " ".join(a[max(0, i1-6):i1])
    print(f"[{op}] ...{ctx[-60:]} | -{old[:300]} | +{new[:300]}")
    n += 1
    if n >= maxn: break
