#!/usr/bin/env python3
"""AI Scraper — runs inside Docker container, outputs JSON to /data/intel/scrape/"""
import json, os, re, time, urllib.request, urllib.error
from datetime import datetime

OUT = "/data/intel/scrape"
os.makedirs(OUT, exist_ok=True)

def fetch(url, headers=None):
    h = {"User-Agent": "AI-Scraper/1.0"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode()
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}")
        return None

def scrape_github():
    print("Scraping GitHub trending AI repos...")
    data = fetch(
        "https://api.github.com/search/repositories?q=topic:artificial-intelligence+topic:machine-learning&sort=stars&order=desc&per_page=20",
        {"Accept": "application/vnd.github+json"}
    )
    if not data:
        return
    try:
        items = json.loads(data).get("items", [])[:15]
        results = []
        for r in items:
            results.append({
                "name": r["full_name"],
                "stars": r["stargazers_count"],
                "description": (r.get("description") or "")[:120],
                "language": r.get("language", ""),
                "updated": r["updated_at"]
            })
        path = os.path.join(OUT, f"github-ai-{datetime.now():%Y%m%d-%H}.json")
        with open(path, "w") as f:
            json.dump(results, f, indent=2)
        print(f"  Saved {len(results)} repos to {path}")
    except Exception as e:
        print(f"  ERROR parsing GitHub: {e}")

def scrape_arxiv():
    print("Scraping arXiv AI papers...")
    data = fetch(
        "http://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL&sortBy=submittedDate&sortOrder=descending&max_results=15"
    )
    if not data:
        return
    try:
        results = []
        for entry in re.finditer(r"<entry>(.*?)</entry>", data, re.DOTALL):
            title_m = re.search(r"<title>(.*?)</title>", entry.group(1), re.DOTALL)
            summary_m = re.search(r"<summary>(.*?)</summary>", entry.group(1), re.DOTALL)
            published_m = re.search(r"<published>(.*?)</published>", entry.group(1))
            if title_m:
                results.append({
                    "title": re.sub(r"\s+", " ", title_m.group(1).strip())[:200],
                    "published": published_m.group(1) if published_m else "",
                    "summary": re.sub(r"\s+", " ", (summary_m.group(1) if summary_m else "").strip())[:200]
                })
        path = os.path.join(OUT, f"arxiv-ai-{datetime.now():%Y%m%d-%H}.json")
        with open(path, "w") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"  Saved {len(results)} papers to {path}")
    except Exception as e:
        print(f"  ERROR parsing arXiv: {e}")

def scrape_perks():
    print("Scraping getaiperks.com...")
    data = fetch("https://www.getaiperks.com/api/perks")
    if not data:
        return
    try:
        perks = json.loads(data).get("perks", [])
        path = os.path.join(OUT, f"perks-{datetime.now():%Y%m%d}.json")
        with open(path, "w") as f:
            json.dump(perks, f, indent=2)
        print(f"  Saved {len(perks)} perks to {path}")
    except Exception as e:
        print(f"  ERROR parsing perks: {e}")

if __name__ == "__main__":
    while True:
        print(f"\n[{datetime.now():%Y-%m-%d %H:%M:%S}] Starting scrape cycle...")
        scrape_github()
        scrape_arxiv()
        # Only scrape perks once per day (at 8am UTC)
        if datetime.now().hour == 8:
            scrape_perks()
        print("Done. Sleeping 1 hour...")
        time.sleep(3600)
