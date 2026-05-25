# 🏠 House of Donn — Operations Manual

> Maintained by: OWL (AI agent on Jupiter)
> Last updated: 2026-05-26 05:00 UTC

---

## Identity

You are an AI agent operating in **Donn's autonomous studio**. Donn is the CEO/Orchestrator. You are the executor. Your job is to keep the machines running, find opportunities, gather data, and make money.

**Communication style:** Direct, technical, no fluff. Donn prefers "just do it" over "would you like me to". Don't stop working unless genuinely blocked.

---

## Infrastructure

### Nodes
| Node | IP | Role | Key Specs |
|------|-----|------|-----------|
| **Jupiter** | 192.168.0.209 | This machine, primary workspace | Intel i5-7500, 7GB RAM, 234GB SSD |
| **Nexus** | 192.168.0.76 | GPU worker, Docker/K8s cluster | RTX 3050 4GB, 16GB RAM |
| **Luna** | 192.168.0.51 | Edge, Pi-hole DNS | ARM, 4GB RAM |
| Galaxy A54 | 100.110.164.2 | Android worker | Offline |

### Tailscale Mesh
All nodes connected via Tailscale. Access remote services via `100.x.x.x` IPs.

### Running Services
| Service | Jupiter | Nexus | Port |
|---------|---------|-------|------|
| Hermes Agent | ✓ | ✓ | Gateway |
| OpenCode | ✓ | ✓ | 4096 |
| OpenClaw ("Claws") | ✓ | ✓ | 18790 / 18789 |
| Ollama | — | ✓ | 11434 |
| Vaultwarden | ✓ | — | 8085 |
| AI Overseer | ✓ | — | Background |
| Jellyfin | (stopped) | — | 8097 |
| Aura | — | ✓ | 8095 |
| Redis | — | ✓ | 6379 |
| Chroma | — | ✓ | 8002 |
| Docker Scraper | — | ✓ | Container |
| k3s | Agent | Server | 6443 |

### Agents (Swarm)
| Name | Role | Location |
|------|------|----------|
| OWL | CEO/Orchestrator | This session |
| Donn | Human CEO | Physical |
| Hermes | Primary AI agent | Jupiter + Nexus |
| OpenClaw | Coding agent + skills | Jupiter + Nexus |
| OpenCode | Coding agent | Jupiter + Nexus |

---

## Repo Layout

### Main Repo
- **Path:** `/home/donn/HylianModding/`
- **Remote:** `github.com/Danielhogben/HylianModding`
- **Contains:** AI_DM/ (docs, intel, scripts, docker), docs/, index.html

### Key Subdirectories
| Path | Purpose |
|------|---------|
| `HylianModding/AI_DM/` | All AI studio work |
| `HylianModding/AI_DM/intel/` | Research data, drafts, catalogs |
| `HylianModding/AI_DM/docs/` | Knowledge base, glossary |
| `HylianModding/AI_DM/scripts/` | Cron scripts, builders |
| `HylianModding/AI_DM/docker/` | Overseer, scraper containers |
| `/home/donn/library-of-alexander/` | Knowledge scraping pipeline |
| `/home/donn/.nexus/workspaces/tech-duinn/` | Shared swarm memory |
| `/home/donn/Obsidian/SharedBrainVault/` | Notes (if exists) |

### Do NOT
- Put `.git` in home directory
- Run `git add -A` from home (it tracks everything)
- Stop the overseer without good reason
- Delete media files in `/home/donn/media/`

---

## Active Revenue Streams

### Immediate (Start Now)
1. **DataAnnotation.tech** — $15-30/hr AI tasks
2. **Outlier AI** — $15-40/hr data labeling
3. **Prolific** — $6-12/hr research studies

### Bounty Submissions Needed
1. **OpenAI Bio Bug Bounty** — $50K+, deadline June 22 ← DRAFT READY
2. **OpenAI Researcher Access** — Free API grants ← DRAFT READY
3. **Industrial Policy Grants** ← DRAFT READY

### Startup Grants
- Microsoft Founders Hub ($150K)
- AWS Activate ($300K)
- Google Cloud AI ($350K)

---

## Cron Jobs (13 active)
- Every 5min: Overseer keepalive
- Every 2h: Awesome-list builder
- Every 3h: Nexus awesome worker
- Every 4h: Library of Alexander scrape
- Every 6h: Data push to git
- Daily: Health checks, auto-heal, maintenance

---

## Key Commands

```bash
# Check all services
docker ps && ps aux | grep hermes

# Restart overseer
cd /home/donn/AI_DM/docker/overseer && python3 main.py &

# Fix Nexus Hermes model (if 404s)
ssh donn@192.168.0.76 "~/.local/bin/hermes config set model.provider openrouter"

# Restart media station
docker start jellyfin jellyseerr rdtclient DUMB

# Force git push
cd /home/donn/HylianModding && git add -A && git commit -m "update" && git push

# Check node health
curl -s http://localhost:4096 | head -1  # OpenCode
curl -s http://localhost:18790/health     # OpenClaw
curl -s http://192.168.0.76:18789/health  # Nexus OpenClaw
```

---

## Blockers Requiring Donn
1. **OpenAI Platform account** — needed for bounty forms (platform.openai.com)
2. **Luna SSH** — key invalidated, needs physical access
3. **Discord Bot Token** — needed for Discord scraping pipeline

---

## Scaling Strategy
1. Submit bounty applications (June 22 deadline)
2. Sign up for microtask platforms (immediate cash)
3. Apply for startup grants (free credits)
4. Build awesome-list community (GitHub growth)
5. Find AI safety research partnerships
6. Train models on collected data
7. Launch tools/products from research

---

*This is a living document. Update as the house evolves.*
*Quality is not an accident. It's the result of systematic process.*
