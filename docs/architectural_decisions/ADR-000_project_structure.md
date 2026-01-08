# ADR-000: Project Structure and Development Concept

**Date**: 2026-01-06
**Status**: Foundation Document
**Type**: Seed ADR (Explains project structure in context of environment)

## Overview

This document explains how this project operates within the OneCred tiered development environment.

## Project Structure

### This Project is Self-Contained
```
active-project/
├── cert/       # YOUR certificates (don't look in parent dirs)
├── logs/       # YOUR logs (write here, not /workspace/logs)
├── data/       # YOUR data files (input/output/temp)
├── scripts/    # YOUR automation scripts
├── tools/      # Links to environment tools (jira, mongo, etc.)
├── docs/       # YOUR documentation and decisions
├── src/        # YOUR source code
└── tests/      # YOUR tests
```

### Understanding the Tiers

**You are HERE** → Project Level (`/workspace/src/active-project/`)
- This is YOUR workspace
- Everything you need is in THIS directory
- Your code, your data, your logs

**Above you** → Environment Level (`/workspace/`)
- Development tools and utilities
- Shared templates
- Infrastructure configuration
- You can ACCESS tools but don't MODIFY environment

## Key Principles for Development

### 1. Use Local Resources FIRST
```bash
# GOOD - Use project resources
./cert/.env               # Your project secrets
./logs/app.log            # Your project logs
./data/input.csv          # Your project data

# AVOID - Don't reach up to parent
../../../cert/.env        # Environment secrets
/workspace/logs/          # Environment logs
```

### 2. Access Tools via Symlinks
```bash
# Tools are linked in ./tools/ for convenience
./tools/jira-pull TICKET-123     # Pull JIRA tickets
./tools/mongo-connect             # Connect to MongoDB
./tools/env-check                 # Validate setup
```

### 3. Resource Resolution Order
1. Check project directory first (`./cert/api_key.txt`)
2. Fall back to environment if absolutely needed
3. Document any environment dependencies

## Common Tasks

### Starting Work
1. Check your project CLAUDE.md for context
2. Pull latest ticket: `./tools/jira-pull TICKET-XXX`
3. Work in `./src/` directory
4. Write logs to `./logs/`
5. Save data to `./data/`

### Adding Secrets/Configs
1. Copy `./cert/.env.template` to `./cert/.env`
2. Fill in YOUR project values
3. Never commit `.env` (it's gitignored)

### Running Your Application
```bash
# Load your project environment
source ./cert/.env

# Run with your project resources
python src/main.py \
    --config ./cert/config.json \
    --data ./data/input/ \
    --output ./data/output/ \
    --log ./logs/app.log
```

## Quick Reference

| What | Where | Example |
|------|-------|---------|
| Your code | `./src/` | `./src/main.py` |
| Your tests | `./tests/` | `./tests/test_main.py` |
| Your configs | `./cert/` | `./cert/.env` |
| Your logs | `./logs/` | `./logs/debug.log` |
| Your data | `./data/` | `./data/dataset.csv` |
| Your scripts | `./scripts/` | `./scripts/deploy.sh` |
| Env tools | `./tools/` | `./tools/jira-pull` |
| Your docs | `./docs/` | `./docs/ARCHITECTURE.md` |

## Remember

✅ **DO**: Keep everything in your project directory
✅ **DO**: Use the tools via `./tools/` symlinks
✅ **DO**: Document project-specific decisions in `./docs/architectural_decisions/`

❌ **DON'T**: Use `../` paths to access parent directories
❌ **DON'T**: Write to `/workspace/` directories
❌ **DON'T**: Assume environment resources exist

## Next Steps

1. Read `./CLAUDE.md` for project-specific instructions
2. Check `./docs/ARCHITECTURE.md` for system design
3. Review other ADRs in `./docs/architectural_decisions/`
4. Start coding in `./src/`!

---
*This is a seed document explaining the project structure. Add your project-specific ADRs starting with ADR-001.*
