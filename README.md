# HylianModding

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.1-blue?style=for-the-badge" alt="Version 1.0.1" />
  <img src="https://img.shields.io/badge/platform-N64%20%7C%20SNES%20%7C%20GBA%20%7C%20Multi-green?style=for-the-badge" alt="Platforms" />
  <img src="https://img.shields.io/badge/license-MIT-purple?style=for-the-badge" alt="MIT License" />
</p>

<p align="center">
  <strong>Autonomous Game Studio — N64 ROM Hacking & Game Development</strong><br />
  <em>Building retro game mods, AI-powered game engines, and open toolchains.</em</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-directory-structure">Structure</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-contributing">Contributing</a> •
  <a href="#-license">License</a>
</p>

---

## 🎮 About

HylianModding is an autonomous game development studio focused on retro game modification, N64 ROM hacking, and game engine development. The project combines AI-powered tooling with traditional reverse engineering to create mods for classic games like Ocarina of Time, Majora's Mask, and original titles.

**Version 1.0.1** — Initial public release showcasing the core toolchain and active projects.

## ✨ Features

- **AI Dungeon Master** — AI-powered N64 game engine (AI_DM)
- **Co-op Framework** — Networked co-op gameplay framework (CoOp)
- **ROM Hacking Toolkit** — N64 ROM modification and asset extraction tools
- **Game Engine** — Custom 3D game engine (GameForge)
- **Modding Tools** — Fast64, Zelda64Recomp, N64Recomp integration
- **Asset Pipeline** — Automated asset conversion and optimization
- **ML Ops** — Local LLM training and fine-tuning for game AI

## 📁 Directory Structure

```
HylianModding/
├── AI_DM/              # AI Dungeon Master — N64 AI game engine
├── AI_Assets/          # AI-generated game assets
├── AI_Control/         # AI control systems
├── AI_World/           # AI world generation
├── Assets/             # Shared game assets (models, textures, patches)
├── BigBangSaga/        # Big Bang Saga game project
├── CoOp/               # Co-op game framework
├── Donn/               # Personal projects and builds
├── Game/               # Game project files
├── Game3D/             # 3D game development
├── GameForge/          # Custom game engine
├── Library/            # ROM library and metadata
├── Metadata/           # Game metadata (GameBanana, Spriters Resource)
├── ModLoader64/        # ModLoader64 integration
├── MySpaceShooter/     # Space shooter game project
├── MyWorld/            # World building project
├── NuclearMon/         # NuclearMon game project
├── ROM_Hacks/          # ROM hack projects
│   ├── Crystal_Clocks/
│   ├── Demons_Quest/
│   ├── Majoras_Mask_Chaos_Edition/
│   ├── Master_of_Time_Revisited/
│   └── ...
├── ScraperBot/         # Web scraping bot for game resources
├── ShipOfHarkinian/    # Ship of Harkinian mods
├── StellarMon/         # StellarMon game project
├── Studio/             # Game studio engine and toolchains
├── SwarmCoordinator/   # Docker Swarm coordination
├── Tools/              # N64 development tools (Fast64, Project CTR, etc.)
├── disasm/             # Disassembly projects
├── docs/               # Documentation and showcase site
├── lib/                # Shared libraries
├── scripts/            # Utility scripts
├── tools/              # Additional tools (N64Recomp, Zelda64Recomp, etc.)
├── venv/               # Python virtual environment
├── .github/            # GitHub Actions CI/CD workflows
├── .gitignore          # Git ignore rules
├── CONTRIBUTING.md     # Contribution guidelines
├── LICENSE             # MIT License
└── README.md           # This file
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.11+** — Core tooling and AI engine
- **Docker & Docker Compose** — Containerized services and swarm
- **N64 SDK** — For ROM compilation (libultra or modern alternatives)
- **Blender 3.6+** — 3D asset creation and export
- **Git LFS** — For large asset files

### Quick Start

```bash
# Clone the repository
git clone https://github.com/donn-duinn/HylianModding.git
cd HylianModding

# Set up Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Explore the projects
ls AI_DM/        # AI Dungeon Master
ls CoOp/         # Co-op framework
ls ROM_Hacks/    # ROM hack projects
ls Tools/        # N64 dev tools
```

### Running the AI Engine

```bash
cd AI_DM
python brain.py --mode=interactive
```

### Building a ROM Hack

```bash
cd ROM_Hacks/Crystal_Clocks
make setup
make build
```

## 🛠 Tech Stack

| Category | Technologies |
|----------|-------------|
| **Languages** | Python, C/C++, MIPS Assembly, GLSL |
| **AI/ML** | PyTorch, Unsloth, llama.cpp, DSPy |
| **Game Dev** | Fast64, Blender, N64Recomp, Zelda64Recomp |
| **Infrastructure** | Docker Swarm, Tailscale, Pi-hole, K3s |
| **CI/CD** | GitHub Actions, pre-commit |
| **Platforms** | N64, SNES, GBA, Genesis, PS1, Dreamcast |

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## 📜 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- **decomp.dev** — N64 reverse engineering community
- **Zelda64Recomp** — Zelda 64 recompilation project
- **Fast64** — Blender N64 plugin
- **libultra** — N64 SDK reference

---

<p align="center">
  <sub>Built with ❤️ by the HylianModding Autonomous Studio</sub><br />
  <sub>Version 1.0.1 — May 2026</sub>
</p>
