#!/bin/bash
# Scraper loop — runs forever inside Docker
# Fetches: GitHub trends, arXiv papers, perk sites

INTEL_DIR="/data/intel/scrape"
mkdir -p "$INTEL_DIR"

log() { echo "[$(date -Iseconds)] $1"; }

while true; do
  # 1. GitHub trending AI repos
  log "Scraping GitHub trending..."
  curl -s "https://api.github.com/search/repositories?q=topic:artificial-intelligence+topic:machine-learning&sort=stars&order=desc&per_page=20" \
    -H "Accept: application/vnd.github+json" \
    | python3 -c "
import sys, json
data = json.load(sys.stdin)
items = data.get('items', [])
for r in items[:10]:
    print(json.dumps({
        'name': r['full_name'],
        'stars': r['stargazers_count'],
        'description': r.get('description','')[:100],
        'updated': r['updated_at']
    }))
" > "$INTEL_DIR/github-ai-$(date +%Y%m%d-%H).json" 2>/dev/null

  # 2. arXiv AI papers
  log "Scraping arXiv..."
  curl -s "http://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL&sortBy=submittedDate&sortOrder=descending&max_results=10" \
    | python3 -c "
import sys, re
content = sys.stdin.read()
for entry in re.finditer(r'<entry>(.*?)</entry>', content, re.DOTALL):
    title = re.search(r'<title>(.*?)</title>', entry.group(1), re.DOTALL)
    summary = re.search(r'<summary>(.*?)</summary>', entry.group(1), re.DOTALL)
    published = re.search(r'<published>(.*?)</published>', entry.group(1))
    if title:
        print(json.dumps({
            'title': title.group(1).strip()[:200].replace('\n',' '),
            'published': published.group(1) if published else '',
            'summary': (summary.group(1).strip()[:150].replace('\n',' ')) if summary else ''
        }, ensure_ascii=False))
" > "$INTEL_DIR/arxiv-ai-$(date +%Y%m%d-%H).json" 2>/dev/null

  # 3. Check getaiperks.com for new perks (daily)
  if [ "$(date +%H)" = "08" ]; then
    log "Scraping getaiperks..."
    curl -s "https://www.getaiperks.com/api/perks" \
      -H "User-Agent: Mozilla/5.0" \
      | python3 -c "import sys,json; d=json.load(sys.stdin); [print(json.dumps(p)) for p in d.get('perks',[])]" \
      > "$INTEL_DIR/perks-$(date +%Y%m%d).json" 2>/dev/null
  fi

  log "Done. Sleeping 1 hour..."
  sleep 3600
done
