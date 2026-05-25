#!/usr/bin/env python3
"""Search HuggingFace for jailbreak-related models, datasets, and tools."""

import json
import time
import sys
from huggingface_hub import HfApi

api = HfApi()

# Core search keywords
KEYWORDS_MODELS = [
    "jailbreak",
    "redteam",
    "red team",
    "adversarial",
    "bypass",
    "uncensored",
    "poison",
    "backdoor",
    "attack",
]

KEYWORDS_DATASETS = [
    "jailbreak",
    "redteam",
    "red team",
    "adversarial",
    "bypass",
    "uncensored",
    "safety",
    "alignment",
    "poison",
    "backdoor",
    "attack",
    "harmful",
    "toxic",
]

# Relevance filter: items must match these themes to be catalogued
RELEVANCE_POSITIVE = [
    "jailbreak", "red team", "redteam", "adversarial prompt", "safety bypass",
    "uncensored model", "model poisoning", "backdoor attack", "harmful prompt",
    "attack prompt", "llm attack", "prompt injection", "safety evaluation",
    "alignment benchmark", "harmful behavior", "toxic content", "refusal",
    "safety guardrail", "safety classifier", "harmbench", "advbench",
    "safebench", "safety benchmark", "red-teaming", "red teaming",
    "adversarial attack", "adversarial robustness",
]

# Items to exclude (too generic, not relevant)
RELEVANCE_NEGATIVE = [
    "jailbreak"  # will filter specific ones positively if they match
]

catalog = {
    "metadata": {
        "search_date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "keywords_used": {
            "models": KEYWORDS_MODELS,
            "datasets": KEYWORDS_DATASETS,
        },
        "total_results_raw": {},
        "total_catalogued": {},
    },
    "models": [],
    "datasets": [],
}

def score_relevance(name, tags, description):
    """Score how relevant an item is to jailbreak/redteam/attack research."""
    text = f"{name} {description} {' '.join(tags)}".lower()
    score = 0
    matches = []
    for kw in RELEVANCE_POSITIVE:
        if kw in text:
            score += 1
            matches.append(kw)
    return score, matches

def is_noteworthy(name, tags, description, downloads, likes):
    """Determine if an item is worth cataloguing."""
    text = f"{name} {description} {' '.join(tags)}".lower()
    
    # Must have at least some relevance
    score, matches = score_relevance(name, tags, description)
    if score == 0:
        return False
    
    # Require minimum engagement or high relevance
    if score >= 3:
        return True
    if score >= 2 and (downloads > 100 or likes > 2):
        return True
    if score >= 1 and (downloads > 1000 or likes > 10):
        return True
    
    return False

def safe_get(obj, *keys, default=""):
    """Safely traverse nested dicts."""
    for k in keys:
        try:
            obj = obj[k]
        except (KeyError, IndexError, TypeError):
            return default
    return obj if obj is not None else default

def sanitize(text, max_len=500):
    return str(text)[:max_len] if text else ""

# ── Search models ──
print("=== Searching MODELS ===")
seen_model_ids = set()

for kw in KEYWORDS_MODELS:
    print(f"  Searching models for: '{kw}'")
    try:
        results = list(api.list_models(
            search=kw,
            sort="downloads",
            direction=-1,
            limit=100,
        ))
        catalog["metadata"]["total_results_raw"][f"models:{kw}"] = len(results)
        
        for m in results:
            model_id = m.modelId
            if model_id in seen_model_ids:
                continue
            
            desc = sanitize(m.pipeline_tags or safe_get(m, 'cardData', 'description', default=""))
            tags = list(m.tags) if m.tags else []
            
            if is_noteworthy(model_id, tags, desc, m.downloads or 0, m.likes or 0):
                seen_model_ids.add(model_id)
                entry = {
                    "id": model_id,
                    "type": "model",
                    "downloads": m.downloads or 0,
                    "likes": m.likes or 0,
                    "tags": tags,
                    "description": desc or sanitize(m.card_data or "", max_len=300),
                    "pipeline_tag": m.pipeline_tag or safe_get(m, 'pipeline_tags', default=""),
                    "url": f"https://huggingface.co/{model_id}",
                    "matched_keyword": kw,
                    "relevance_score": score_relevance(model_id, tags, desc)[0],
                }
                catalog["models"].append(entry)
                print(f"    [+] {model_id} (score={entry['relevance_score']}, downloads={entry['downloads']})")
        
        time.sleep(0.3)  # rate limit avoidance
    except Exception as e:
        print(f"    [ERROR] searching models '{kw}': {e}")
        catalog["metadata"]["total_results_raw"][f"models:{kw}_error"] = str(e)[:200]

# ── Search datasets ──
print("=== Searching DATASETS ===")
seen_ds_ids = set()

for kw in KEYWORDS_DATASETS:
    print(f"  Searching datasets for: '{kw}'")
    try:
        results = list(api.list_datasets(
            search=kw,
            sort="downloads",
            direction=-1,
            limit=100,
        ))
        catalog["metadata"]["total_results_raw"][f"datasets:{kw}"] = len(results)
        
        for ds in results:
            ds_id = ds.id
            if ds_id in seen_ds_ids:
                continue
            
            desc = sanitize(safe_get(ds, 'cardData', 'description', default=""))
            tags = list(ds.tags) if ds.tags else []
            
            if is_noteworthy(ds_id, tags, desc, ds.downloads or 0, ds.likes or 0):
                seen_ds_ids.add(ds_id)
                entry = {
                    "id": ds_id,
                    "type": "dataset",
                    "downloads": ds.downloads or 0,
                    "likes": ds.likes or 0,
                    "tags": tags,
                    "description": desc or sanitize(ds.card_data or "", max_len=300),
                    "url": f"https://huggingface.co/datasets/{ds_id}",
                    "matched_keyword": kw,
                    "relevance_score": score_relevance(ds_id, tags, desc)[0],
                }
                catalog["datasets"].append(entry)
                print(f"    [+] {ds_id} (score={entry['relevance_score']}, downloads={entry['downloads']})")
        
        time.sleep(0.3)
    except Exception as e:
        print(f"    [ERROR] searching datasets '{kw}': {e}")
        catalog["metadata"]["total_results_raw"][f"datasets:{kw}_error"] = str(e)[:200]

# ── Summary ──
catalog["metadata"]["total_catalogued"] = {
    "models": len(catalog["models"]),
    "datasets": len(catalog["datasets"]),
    "total": len(catalog["models"]) + len(catalog["datasets"]),
}

# Sort by relevance score then downloads
catalog["models"].sort(key=lambda x: (-x["relevance_score"], -x["downloads"]))
catalog["datasets"].sort(key=lambda x: (-x["relevance_score"], -x["downloads"]))

print(f"\n=== SUMMARY ===")
print(f"  Models catalogued:   {len(catalog['models'])}")
print(f"  Datasets catalogued: {len(catalog['datasets'])}")
print(f"  Total:               {catalog['metadata']['total_catalogued']['total']}")

# Write output
output_path = "/home/donn/AI_DM/intel/huggingface_jailbreak_catalog.json"
with open(output_path, "w") as f:
    json.dump(catalog, f, indent=2, default=str)

print(f"\nCatalog written to: {output_path}")