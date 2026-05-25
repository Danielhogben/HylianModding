#!/usr/bin/env python3
"""
AI Overseer + Watchdog System
- Monitors Hermes agents across all nodes
- Detects inactivity and restarts stuck agents
- Runs data pipelines (Discord, YouTube, University scraping)
- Browser automation for data collection
- Self-healing: can fix common issues without human input
"""
import os, sys, json, time, re, subprocess, threading, logging, signal
from datetime import datetime, timedelta
from pathlib import Path
import urllib.request
import schedule
import requests
import psutil

# ═══════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════

NODES = {
    "jupiter": {"ip": "192.168.0.209", "local": True, "hermes_port": None, "opencode_port": 4096, "openclaw_port": 18790},
    "nexus": {"ip": "192.168.0.76", "local": False, "hermes_port": None, "opencode_port": 4096, "openclaw_port": 18789},
}

INACTIVITY_TIMEOUT = 600  # 10 minutes without activity = stuck
CHECK_INTERVAL = 60       # Check every minute
MAX_RESTARTS = 5          # Max restarts per hour before escalating

INTEL_DIR = Path("/home/donn/AI_DM/intel")
INTEL_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = Path("/home/donn/AI_DM/intel/overseer.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(str(LOG_FILE)),
        logging.StreamHandler(sys.stdout)
    ]
)
log = logging.getLogger("overseer")

# Track agent activity
agent_state = {
    node: {
        "last_activity": datetime.utcnow(),
        "restart_count": 0,
        "status": "unknown",
        "errors": []
    }
    for node in NODES
}

# ═══════════════════════════════════════════════════════════
# HEALTH CHECKS
# ═══════════════════════════════════════════════════════════

def check_node_health(node_name, node_config):
    """Check if a node's agents are healthy and active."""
    results = {}
    
    if node_config["local"]:
        # Local checks
        results["opencode"] = check_port(4096)
        results["openclaw"] = check_port(18790)
        results["hermes"] = check_process("hermes")
        results["docker"] = check_docker()
        results["disk_ok"] = psutil.disk_usage("/").percent < 90
        results["mem_ok"] = psutil.virtual_memory().percent < 90
    else:
        # Remote checks via HTTP
        for service, port in [("opencode", 4096), ("openclaw", 18789)]:
            results[service] = check_remote_port(node_config["ip"], port)
        
        # Check if docker is running on remote
        try:
            r = requests.get(f"http://{node_config['ip']}:2375/containers/json", timeout=5)
            results["docker"] = r.status_code == 200
        except:
            results["docker"] = False
        
        results["disk_ok"] = True  # Can't check remotely without SSH
        results["mem_ok"] = True
    
    healthy = all(v for k, v in results.items() if k not in ["disk_ok", "mem_ok"])
    return healthy, results


def check_port(port, host="localhost"):
    """Check if a port is open."""
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((host, port))
        s.close()
        return True
    except:
        return False


def check_remote_port(ip, port):
    """Check if a remote port is open."""
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False


def check_process(name):
    """Check if a process is running."""
    for proc in psutil.process_iter(["name", "cmdline"]):
        try:
            if name in " ".join(proc.info["cmdline"] or []).lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False


def check_docker():
    """Check if Docker daemon is running."""
    try:
        subprocess.run(["docker", "ps"], capture_output=True, timeout=5, check=True)
        return True
    except:
        return False


# ═══════════════════════════════════════════════════════════
# WATCHDOG — Detect and fix stuck agents
# ═══════════════════════════════════════════════════════════

def watchdog_check():
    """Run watchdog checks on all nodes."""
    log.info("=== Watchdog check cycle ===")
    
    for node_name, config in NODES.items():
        state = agent_state[node_name]
        
        # Check health
        healthy, details = check_node_health(node_name, config)
        state["status"] = "healthy" if healthy else "unhealthy"
        
        now = datetime.utcnow()
        inactive_time = (now - state["last_activity"]).total_seconds()
        
        log.info(f"  {node_name}: {state['status']} | inactive: {inactive_time:.0f}s")
        
        # Check for inactivity
        if inactive_time > INACTIVITY_TIMEOUT:
            log.warning(f"  {node_name}: INACTIVE for {inactive_time:.0f}s — attempting recovery")
            recover_node(node_name, config, state)
        
        # Check for unhealthy services
        if not healthy:
            failed = [k for k, v in details.items() if not v]
            if failed:
                log.warning(f"  {node_name}: Failed services: {failed}")
                for svc in failed:
                    restart_service(node_name, config, svc, state)
        
        # Reset restart count every hour
        if state["restart_count"] > 0 and inactive_time > 3600:
            state["restart_count"] = 0


def recover_node(node_name, config, state):
    """Attempt to recover a stuck node."""
    state["restart_count"] += 1
    state["last_activity"] = datetime.utcnow()
    
    if state["restart_count"] > MAX_RESTARTS:
        log.error(f"  {node_name}: MAX RESTARTS ({MAX_RESTARTS}) exceeded — needs human intervention")
        state["errors"].append(f"{datetime.utcnow().isoformat()}: Max restarts exceeded")
        return
    
    if config["local"]:
        # Local recovery
        log.info(f"  {node_name}: Restarting local services...")
        restart_service(node_name, config, "hermes", state)
        restart_service(node_name, config, "openclaw", state)
    else:
        # Remote recovery via HTTP API or Docker
        log.info(f"  {node_name}: Remote recovery for {config['ip']}")
        # Restart Docker containers on remote
        try:
            # Try to restart via Docker API
            r = requests.post(f"http://{config['ip']}:2375/containers/jellyfin/restart", timeout=10)
            log.info(f"  {node_name}: Remote restart result: {r.status_code}")
        except Exception as e:
            log.warning(f"  {node_name}: Remote recovery failed: {e}")
    
    state["last_activity"] = datetime.utcnow()


def restart_service(node_name, config, service, state):
    """Restart a specific service."""
    log.info(f"  Restarting {service} on {node_name}...")
    state["last_activity"] = datetime.utcnow()
    
    try:
        if service == "openclaw":
            if config["local"]:
                subprocess.run(["systemctl", "--user", "restart", "openclaw-gateway"], 
                             capture_output=True, timeout=10)
            # Remote: can't restart without SSH
            
        elif service == "hermes":
            # Hermes is a gateway process — can't easily restart without knowing PID
            log.info(f"  Hermes restart on {node_name} requires manual intervention or session reset")
        
        elif service == "docker":
            if config["local"]:
                subprocess.run(["systemctl", "restart", "docker"], capture_output=True, timeout=15)
        
        elif service in ["opencode", "openclaw"]:
            port = config.get(f"{service}_port")
            if port and not check_port(port):
                log.warning(f"  {service} on port {port} is down")
                
    except Exception as e:
        log.error(f"  Failed to restart {service} on {node_name}: {e}")


# ═══════════════════════════════════════════════════════════
# DATA PIPELINES
# ═══════════════════════════════════════════════════════════

def pipeline_discord_scraper():
    """Scrape Discord servers for AI/ML research discussions."""
    log.info("Pipeline: Discord scraper")
    
    output = INTEL_DIR / "discord"
    output.mkdir(exist_ok=True)
    
    # Target servers: AI research, ML, security, reverse engineering
    target_servers = [
        "AI Research", "Machine Learning", "Cybersecurity",
        "Reverse Engineering", "LLM Safety", "Red Team",
    ]
    
    # Use discord.py to join and scrape (requires bot token)
    discord_token = os.environ.get("DISCORD_BOT_TOKEN", "")
    if not discord_token:
        log.warning("Discord pipeline: No BOT_TOKEN set — skipping")
        return
    
    try:
        import discord
        # Note: This would need a proper Discord bot setup
        # For now, log that it needs configuration
        log.info(f"Discord pipeline: Would scrape {len(target_servers)} servers")
        (output / "README.md").write_text(
            f"# Discord Scrape Targets\n\n" + 
            "\n".join(f"- {s}" for s in target_servers) +
            f"\n\nToken configured: {'Yes' if discord_token else 'No'}\n"
        )
    except ImportError:
        log.warning("discord.py not installed")


def pipeline_youtube_scraper():
    """Scrape YouTube channels for AI/ML content."""
    log.info("Pipeline: YouTube scraper")
    
    output = INTEL_DIR / "youtube"
    output.mkdir(exist_ok=True)
    
    # Target channels for AI/ML content
    channels = [
        # AI Research
        "@3blue1brown", "@YannicKilcher", "@TwoMinutePapers",
        "@ArxivInsights", "@AIExplained", "@sentdex",
        # ML Engineering  
        "@HuggingFace", "@OpenAI", "@AnthropicAI",
        "@GoogleDeepMind", "@MistralAI", "@cohere",
        # Security / Red Team
        "@LiveOverflow", "@JohnHammond", "@IppSec",
        # Reverse Engineering
        "@OALabs", "@GynvaelEN", "@hasherezade",
    ]
    
    results = []
    for channel in channels[:5]:  # Limit per run to avoid rate limiting
        try:
            # Use youtube-transcript-api via subprocess
            result = subprocess.run(
                ["python3", "-c", f"""
from youtube_transcript_api import YouTubeTranscriptApi
import json, urllib.request

# Get channel videos
try:
    # Search for channel videos
    search_url = "https://www.youtube.com/results?search_query=AI+machine+learning+research+2026"
    req = urllib.request.Request(search_url, headers={{"User-Agent": "Mozilla/5.0"}})
    # This is a simplified approach — real implementation would use YouTube Data API
    print(json.dumps({{"channel": "{channel}", "status": "needs_api_key"}}))
except Exception as e:
    print(json.dumps({{"channel": "{channel}", "error": str(e)}}))
"""],
                capture_output=True, text=True, timeout=10
            )
            try:
                data = json.loads(result.stdout.strip().split('\n')[-1])
                results.append(data)
            except:
                results.append({"channel": channel, "status": "parse_error"})
        except Exception as e:
            results.append({"channel": channel, "error": str(e)})
        
        time.sleep(2)  # Rate limiting
    
    # Save results
    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M")
    (output / f"channels-{timestamp}.json").write_text(json.dumps(results, indent=2))
    log.info(f"YouTube pipeline: Processed {len(results)} channels")


def pipeline_university_scraper():
    """Scrape university websites for AI/ML course materials and datasets."""
    log.info("Pipeline: University scraper")
    
    output = INTEL_DIR / "universities"
    output.mkdir(exist_ok=True)
    
    # Target universities with strong AI/ML programs
    targets = [
        {"name": "MIT", "url": "https://www.csail.mit.edu/research", "dept": "CSAIL"},
        {"name": "Stanford", "url": "https://ai.stanford.edu/", "dept": "AI Lab"},
        {"name": "Berkeley", "url": "https://bair.berkeley.edu/", "dept": "BAIR"},
        {"name": "CMU", "url": "https://www.ml.cmu.edu/", "dept": "ML Dept"},
        {"name": "Oxford", "url": "https://www.robots.ox.ac.uk/", "dept": "Robotics"},
        {"name": "Cambridge", "url": "https://www.cst.cam.ac.uk/research", "dept": "CS"},
        {"name": "ETH Zurich", "url": "https://vis.ethz.ch/", "dept": "VIS"},
        {"name": "Toronto", "url": "https://www.cs.toronto.edu/", "dept": "CS"},
        {"name": "Harvard", "url": "https://seas.harvard.edu/computer-science", "dept": "SEAS"},
        {"name": "Caltech", "url": "https://www.cms.caltech.edu/", "dept": "CMS"},
    ]
    
    results = []
    for target in targets:
        try:
            req = urllib.request.Request(
                target["url"],
                headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                content = resp.read().decode("utf-8", errors="ignore")
            
            # Extract links
            links = re.findall(r'href="([^"]+(?:research|paper|dataset|publication)[^"]*)"', content, re.IGNORECASE)
            links = list(set(links))[:20]  # Deduplicate and limit
            
            # Extract emails
            emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', content)
            emails = list(set(e for e in emails if ".edu" in e))[:10]
            
            result = {
                "university": target["name"],
                "url": target["url"],
                "dept": target["dept"],
                "links_found": len(links),
                "emails_found": len(emails),
                "top_links": links[:5],
                "top_emails": emails[:5],
                "content_size": len(content)
            }
            results.append(result)
            log.info(f"  {target['name']}: {len(links)} links, {len(emails)} emails")
            
            time.sleep(3)  # Be polite
            
        except Exception as e:
            log.warning(f"  {target['name']}: ERROR — {e}")
            results.append({"university": target["name"], "error": str(e)})
    
    # Save
    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M")
    (output / f"scrape-{timestamp}.json").write_text(json.dumps(results, indent=2, ensure_ascii=False))
    log.info(f"University pipeline: Scraped {len(results)} universities")


def pipeline_arxiv_scraper():
    """Scrape arXiv for latest AI/ML papers."""
    log.info("Pipeline: arXiv scraper")
    
    output = INTEL_DIR / "arxiv"
    output.mkdir(exist_ok=True)
    
    categories = ["cs.AI", "cs.LG", "cs.CL", "cs.CR", "cs.MA"]
    all_papers = []
    
    for cat in categories:
        try:
            url = f"http://export.arxiv.org/api/query?search_query=cat:{cat}&sortBy=submittedDate&sortOrder=descending&max_results=20"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read().decode()
            
            # Parse Atom XML
            import xml.etree.ElementTree as ET
            root = ET.fromstring(content)
            ns = {"atom": "http://www.w3.org/2005/Atom"}
            
            for entry in root.findall("atom:entry", ns):
                title = entry.find("atom:title", ns)
                summary = entry.find("atom:summary", ns)
                published = entry.find("atom:published", ns)
                
                if title is not None:
                    paper = {
                        "title": title.text.strip().replace("\n", " ")[:200],
                        "published": published.text if published is not None else "",
                        "summary": (summary.text.strip().replace("\n", " ")[:300]) if summary is not None else "",
                        "category": cat
                    }
                    all_papers.append(paper)
            
            log.info(f"  {cat}: Found papers")
            time.sleep(3)  # Rate limit
            
        except Exception as e:
            log.warning(f"  {cat}: ERROR — {e}")
    
    # Save
    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M")
    (output / f"papers-{timestamp}.json").write_text(json.dumps(all_papers, indent=2, ensure_ascii=False))
    log.info(f"arXiv pipeline: Collected {len(all_papers)} papers")


# ═══════════════════════════════════════════════════════════
# WEB DASHBOARD
# ═══════════════════════════════════════════════════════════

def start_dashboard():
    """Start a simple web dashboard for monitoring."""
    from flask import Flask, jsonify, render_template_string
    
    dashboard = Flask("overseer")
    
    HTML = """
    <!DOCTYPE html>
    <html>
    <head><title>AI Overseer Dashboard</title>
    <style>
        body { font-family: monospace; background: #1a1a2e; color: #eee; margin: 20px; }
        .node { background: #16213e; padding: 15px; margin: 10px 0; border-radius: 8px; }
        .healthy { border-left: 4px solid #0f0; }
        .unhealthy { border-left: 4px solid #f00; }
        .warning { border-left: 4px solid #ff0; }
        h1 { color: #e94560; }
        h2 { color: #0f3460; }
        .metric { display: inline-block; margin: 5px 15px; }
        .log { background: #0a0a1a; padding: 10px; max-height: 300px; overflow-y: auto; font-size: 11px; }
    </style>
    </head>
    <body>
    <h1>🧠 AI Overseer Dashboard</h1>
    <p>Last update: {{ timestamp }}</p>
    
    <h2>Nodes</h2>
    {% for name, state in agents.items() %}
    <div class="node {{ state.status }}">
        <h3>{{ name }} ({{ nodes[name].ip }})</h3>
        <div class="metric">Status: <strong>{{ state.status }}</strong></div>
        <div class="metric">Last activity: {{ state.last_activity }}</div>
        <div class="metric">Restarts: {{ state.restart_count }}</div>
    </div>
    {% endfor %}
    
    <h2>Latest Log</h2>
    <div class="log">{{ log_tail }}</div>
    
    <script>setTimeout(() => location.reload(), 30000);</script>
    </body>
    </html>
    """
    
    log.info("Dashboard would start on port 9999")
    # dashboard.run(host="0.0.0.0", port=9999, debug=False)
    # Actually, don't run it here — it blocks the main loop


# ═══════════════════════════════════════════════════════════
# STATE PERSISTENCE
# ═══════════════════════════════════════════════════════════

def save_state():
    """Save overseer state to disk."""
    state_file = INTEL_DIR / "overseer-state.json"
    serializable = {}
    for node, state in agent_state.items():
        serializable[node] = {
            **state,
            "last_activity": state["last_activity"].isoformat()
        }
    state_file.write_text(json.dumps(serializable, indent=2))


def load_state():
    """Load overseer state from disk."""
    state_file = INTEL_DIR / "overseer-state.json"
    if state_file.exists():
        try:
            data = json.loads(state_file.read_text())
            for node, state in data.items():
                if node in agent_state:
                    agent_state[node]["last_activity"] = datetime.fromisoformat(state["last_activity"])
                    agent_state[node]["restart_count"] = state.get("restart_count", 0)
            log.info("Loaded previous state")
        except Exception as e:
            log.warning(f"Failed to load state: {e}")


# ═══════════════════════════════════════════════════════════
# MAIN LOOP
# ═══════════════════════════════════════════════════════════

def main():
    log.info("=" * 60)
    log.info("AI Overseer + Watchdog System Starting")
    log.info("=" * 60)
    
    # Load previous state
    load_state()
    
    # Set up scheduled tasks
    schedule.every(1).minutes.do(watchdog_check)
    schedule.every(2).hours.do(pipeline_arxiv_scraper)
    schedule.every(4).hours.do(pipeline_university_scraper)
    schedule.every(6).hours.do(pipeline_discord_scraper)
    schedule.every(6).hours.do(pipeline_youtube_scraper)
    schedule.every(10).minutes.do(save_state)
    
    # Run initial data pipelines
    log.info("Running initial data pipelines...")
    pipeline_arxiv_scraper()
    
    # Main loop
    log.info("Entering main watchdog loop...")
    while True:
        try:
            schedule.run_pending()
            
            # Always check health
            for node_name, config in NODES.items():
                healthy, details = check_node_health(node_name, config)
                if healthy:
                    agent_state[node_name]["last_activity"] = datetime.utcnow()
                    agent_state[node_name]["status"] = "healthy"
            
            time.sleep(CHECK_INTERVAL)
            
        except KeyboardInterrupt:
            log.info("Shutting down overseer...")
            save_state()
            break
        except Exception as e:
            log.error(f"Main loop error: {e}")
            time.sleep(10)


if __name__ == "__main__":
    main()
