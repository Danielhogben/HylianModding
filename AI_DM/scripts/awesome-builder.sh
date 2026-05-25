#!/bin/bash
# 24/7 Awesome List & AI Knowledge Builder
# Runs every 2 hours on Jupiter
# Works with the Nexus swarm via shared TASKS.md

set -euo pipefail
export PATH="/home/donn/.hermes/hermes-agent/venv/bin:/home/donn/.local/bin:/usr/local/bin:$PATH"
export HOME="/home/donn"

LOG="/home/donn/AI_DM/logs/awesome-builder-$(date +%Y%m%d-%H%M).log"
mkdir -p /home/donn/AI_DM/logs

echo "=== $(date) | Awesome List Builder Start ===" | tee "$LOG"

# 1. Check what's been done
echo "--- Current state ---" | tee -a "$LOG"
cd /home/donn/AI_DM
git pull --rebase 2>&1 | tee -a "$LOG" || true

# 2. Get list of Danielhogben repos
echo "--- Checking for new repos to clone ---" | tee -a "$LOG"
gh repo list Danielhogben --limit 100 --json name 2>/dev/null | python3 -c "
import sys, json, os
repos = json.load(sys.stdin)
cloned = set()
awesome_dir = '/home/donn/AI_DM/awesome-sources'
if os.path.isdir(awesome_dir):
    cloned = set(os.listdir(awesome_dir))
for r in repos:
    name = r['name']
    if name not in cloned:
        print(f'NEED: {name}')
    else:
        print(f'HAVE: {name}')
" 2>&1 | tee -a "$LOG"

# 3. Clone any missing repos
cd /home/donn/AI_DM/awesome-sources 2>/dev/null || mkdir -p /home/donn/AI_DM/awesome-sources && cd /home/donn/AI_DM/awesome-sources

for repo in $(gh repo list Danielhogben --limit 100 --json name -q '.[].name' 2>/dev/null); do
    if [ ! -d "$repo" ]; then
        echo "Cloning $repo..." | tee -a "$LOG"
        git clone --depth 1 "https://github.com/Danielhogben/$repo.git" 2>&1 | tee -a "$LOG" || echo "FAILED: $repo" | tee -a "$LOG"
    fi
done

# 4. Parse all READMEs and build resource index
echo "--- Building resource index ---" | tee -a "$LOG"
python3 << 'PYEOF' 2>&1 | tee -a "$LOG"
import os, json, re

awesome_dir = '/home/donn/AI_DM/awesome-sources'
resources = []

for repo in sorted(os.listdir(awesome_dir)):
    repo_path = os.path.join(awesome_dir, repo)
    if not os.path.isdir(repo_path):
        continue
    
    readme = None
    for candidate in ['README.md', 'readme.md', 'README.rst']:
        candidate_path = os.path.join(repo_path, candidate)
        if os.path.isfile(candidate_path):
            readme = candidate_path
            break
    
    if not readme:
        continue
    
    with open(readme) as f:
        content = f.read()
    
    # Extract links
    links = re.findall(r'\[([^\]]+)\]\((https?://[^\)]+)\)', content)
    
    # Extract description (first paragraph)
    desc_match = re.search(r'#\s+.+?\n\n(.+?)(?:\n\n|\n#)', content, re.DOTALL)
    description = desc_match.group(1).strip()[:200] if desc_match else ""
    
    resources.append({
        'repo': repo,
        'description': description,
        'links': [{'text': t, 'url': u} for t, u in links[:30]],
        'link_count': len(links)
    })

# Save resource index
index_path = '/home/donn/AI_DM/AI_KNOWLEDGE_HUB.json'
with open(index_path, 'w') as f:
    json.dump({
        'generated': '2026-05-26',
        'total_repos': len(resources),
        'total_links': sum(r['link_count'] for r in resources),
        'resources': resources
    }, f, indent=2)

print(f"Indexed {len(resources)} repos, {sum(r['link_count'] for r in resources)} total links")
PYEOF

# 5. Commit and push
cd /home/donn/AI_DM
git add -A 2>&1 | tee -a "$LOG"
git commit -m "auto: awesome-list builder $(date +%Y-%m-%d-%H%M) — indexed repos + resources" 2>&1 | tee -a "$LOG" || echo "Nothing to commit" | tee -a "$LOG"
git push 2>&1 | tee -a "$LOG" || echo "Push failed" | tee -a "$LOG"

# 6. Update Nexus TASKS.md
echo "--- Updating Nexus swarm ---" | tee -a "$LOG"
cat >> /home/donn/.nexus/workspaces/tech-duinn/TASKS.md << 'EOF'

## Auto-Builder Log $(date)
- Cloned new repos to awesome-sources/
- Indexed resources to AI_KNOWLEDGE_HUB.json
- Pushed to git
EOF

echo "=== $(date) | Done ===" | tee -a "$LOG"

# Cleanup old logs (keep last 20)
ls -t /home/donn/AI_DM/logs/awesome-builder-*.log 2>/dev/null | tail -n +21 | xargs rm -f 2>/dev/null || true
