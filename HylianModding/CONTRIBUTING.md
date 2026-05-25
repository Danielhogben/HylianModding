# Contributing to HylianModding

Thank you for your interest in contributing! This document outlines the guidelines and processes for contributing to the HylianModding project.

## Code of Conduct

- Be respectful and constructive
- Focus on what is best for the community and the project
- Show empathy towards other contributors

## How to Contribute

### Reporting Bugs

1. Check if the issue already exists in [Issues](https://github.com/Danielhogben/HylianModding/issues)
2. Use the bug report template when creating a new issue
3. Include: description, steps to reproduce, expected behavior, environment details

### Suggesting Features

1. Use the feature request template
2. Describe the use case and expected behavior
3. Be open to discussion and alternative approaches

### Pull Requests

1. **Fork** the repository (or create a branch if you have write access)
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes** following the coding standards below
4. **Test your changes** locally
5. **Commit** with clear, descriptive messages:
   - `feat: add new ROM extraction tool`
   - `fix: resolve asset pipeline crash on large files`
   - `docs: update getting started guide`
   - `ci: add linting workflow`
6. **Push** to your branch
7. **Open a Pull Request** against `main`

## Coding Standards

### Python
- Follow PEP 8 style guide
- Use type hints for function signatures
- Write docstrings for public functions
- Maximum line length: 120 characters

### C/C++
- Follow the existing code style in each project
- Use meaningful variable and function names
- Comment complex logic

### Commit Messages
Use conventional commits format:
- `feat:` — New feature
- `fix:` — Bug fix
- `docs:` — Documentation changes
- `style:` — Code style changes (formatting, etc.)
- `refactor:` — Code refactoring
- `test:` — Adding or updating tests
- `ci:` — CI/CD changes
- `chore:` — Maintenance tasks

## Project-Specific Guidelines

### ROM Hacking
- Never commit original ROM files — only patches and tools
- Document the base ROM version and region for each hack
- Test builds before submitting

### AI/ML Code
- Document model requirements and training data sources
- Include evaluation metrics for model changes
- Keep model weights out of the repo (use Git LFS or external storage)

### Asset Pipeline
- Use appropriate file formats for each platform
- Optimize assets for target hardware constraints
- Document asset sources and licenses

## Development Setup

```bash
# Clone and setup
git clone https://github.com/Danielhogben/HylianModding.git
cd HylianModding
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run tests
pytest

# Run linting
flake8 .
```

## Release Process

1. Version numbers follow [Semantic Versioning](https://semver.org/)
2. Releases are tagged: `v1.0.1`, `v1.1.0`, `v2.0.0`, etc.
3. Release notes are auto-generated from commit messages
4. Docker images are built and pushed on release

## Questions?

Open a [Discussion](https://github.com/Danielhogben/HylianModding/discussions) or reach out to the maintainers.

---

Thank you for contributing to HylianModding! 🎮
