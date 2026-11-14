#!/bin/bash
# Fetch TTD's public OpenTTD documentation pages into <out-dir>, then extract their text.
#
# usage: TTD_DOCS_UA=<agent user agent> scripts/refresh-docs.sh <out-dir> [url-list-file]
#   Without url-list-file, URLs come from the sitemap, filtered by scripts/scope.txt.
#   With url-list-file, only those URLs are fetched (same safety checks).
#
# Safety (README rule 7): https and the exact host open.thetradedesk.com only, no redirects,
# no cookies, no credentials, no curl config file; the only custom header is the user agent.
# Any non-200 status or a changed effective URL stops the run.
set -euo pipefail

HOST="open.thetradedesk.com"
SITEMAP="https://$HOST/sitemap.xml"
DIR="$(cd "$(dirname "$0")" && pwd)"
OUT="${1:?usage: refresh-docs.sh <out-dir> [url-list-file]}"
LIST="${2:-}"
UA="${TTD_DOCS_UA:?set TTD_DOCS_UA to an honest agent user agent (see README, D3)}"

mkdir -p "$OUT/raw" "$OUT/md"
: > "$OUT/_offhost.log"
touch "$OUT/_status.tsv"

host_ok() {
  [[ "$1" =~ ^https://open\.thetradedesk\.com(/[^[:space:]]*)?$ ]]
}

fetch() {
  local url="$1" dest="$2" res code eff
  if ! host_ok "$url"; then
    printf '000\t%s\t0\n' "$url" >> "$OUT/_status.tsv"
    echo "STOP: refusing off-host or non-https URL: $url" >&2
    exit 2
  fi
  res=$(curl -q -sS --proto =https --proto-redir =https --max-redirs 0 \
    -A "$UA" --max-time 30 -o "$dest.part" -w '%{http_code} %{url_effective}' "$url") || {
    printf 'ERR\t%s\t1\n' "$url" >> "$OUT/_status.tsv"
    rm -f "$dest.part"
    echo "STOP: curl failed for $url" >&2
    exit 3
  }
  code="${res%% *}"
  eff="${res#* }"
  printf '%s\t%s\t1\n' "$code" "$url" >> "$OUT/_status.tsv"
  if [ "$code" != "200" ] || [ "$eff" != "$url" ]; then
    rm -f "$dest.part"
    echo "STOP: $url returned $code (effective URL: $eff)" >&2
    exit 4
  fi
  mv "$dest.part" "$dest"
  sleep 0.3
}

page_name() {
  printf '%s' "${1#*/docsApp/}" | sed 's|[?#].*||; s|/|__|g'
}

if [ -n "$LIST" ]; then
  grep -v '^[[:space:]]*$' "$LIST" > "$OUT/_urls.txt"
else
  fetch "$SITEMAP" "$OUT/_sitemap.xml"
  : > "$OUT/_sitemap_urls.txt"
  python3 -I -c '
import re, sys
for loc in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", open(sys.argv[1], encoding="utf-8").read()):
    print(loc.replace("&amp;", "&"))
' "$OUT/_sitemap.xml" | while IFS= read -r u; do
    if host_ok "$u"; then
      printf '%s\n' "$u" >> "$OUT/_sitemap_urls.txt"
    else
      printf '%s\n' "$u" >> "$OUT/_offhost.log"
    fi
  done
  grep -E -f "$DIR/scope.txt" "$OUT/_sitemap_urls.txt" | sort -u > "$OUT/_urls.txt"
fi

total=$(wc -l < "$OUT/_urls.txt" | tr -d ' ')
echo "in scope: $total, off-host skipped: $(wc -l < "$OUT/_offhost.log" | tr -d ' ')"

n=0
while IFS= read -r u; do
  n=$((n + 1))
  name=$(page_name "$u")
  [ -s "$OUT/raw/$name.page" ] && continue
  fetch "$u" "$OUT/raw/$name.page"
  [ $((n % 50)) -eq 0 ] && echo "fetched $n/$total"
done < "$OUT/_urls.txt"

: > "$OUT/_noarticle.log"
while IFS= read -r u; do
  name=$(page_name "$u")
  rc=0
  python3 -I "$DIR/extract_llm_content.py" "$OUT/raw/$name.page" "$u" > "$OUT/md/$name.md" 2> "$OUT/_extract.err" || rc=$?
  if [ "$rc" -eq 2 ]; then
    rm -f "$OUT/md/$name.md"
    printf '%s\n' "$u" >> "$OUT/_noarticle.log"
  elif [ "$rc" -ne 0 ]; then
    rm -f "$OUT/md/$name.md"
    echo "extractor failed (exit $rc) on $u" >&2
    cat "$OUT/_extract.err" >&2
    exit 1
  fi
done < "$OUT/_urls.txt"

echo "done: $total URLs, no article: $(wc -l < "$OUT/_noarticle.log" | tr -d ' ')"
