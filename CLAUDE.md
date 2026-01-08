# Claude Code Instructions - active-project

## Project Context

**Project**: active-project
**Created**: 2026-01-06
**Active Ticket**: TICKET-XXX
**Repository**: https://github.com/vaishnavi-blauplug/test-setup.git

### IMPORTANT: Claude Code Working Directory Detection

**When working in this project directory (`/workspace/src/active-project/`), Claude MUST:**

1. **Read this CLAUDE.md file FIRST** to understand project-specific context
2. **Check current working directory** with `pwd` to confirm location
3. **Use project-level resources** (./cert/, ./logs/, ./data/) instead of parent directories
4. **Follow project-specific rules** defined in this file
5. **Maintain ADR documentation** for all architectural decisions

**How to verify you're in the right context:**
```bash
# Verify location
pwd  # Should show /workspace/src/active-project

# Verify project files exist
ls -la CLAUDE.md docs/ARCHITECTURE.md

# Check ADR directory
ls docs/architectural_decisions/
```

## Project Structure

This project follows a self-contained architecture with local resources:

```
active-project/
├── cert/                  # Project-specific certificates
├── logs/                  # Project execution logs
├── data/                  # Project datasets
├── scripts/               # Project automation scripts
├── tools/                 # Links to environment tools
├── docs/
│   ├── ARCHITECTURE.md
│   ├── architectural_decisions/
│   └── jira_tickets/
├── src/                  # Source code
├── tests/                # Test files
└── requirements.txt      # Dependencies
```

## Resource Locations

### Project-Level Resources (Primary)
- **Certificates**: `./cert/` - API keys, SSL certs, credentials
- **Logs**: `./logs/` - Application logs, debug output
- **Data**: `./data/` - Datasets, input files, outputs
- **Scripts**: `./scripts/` - Build, deploy, utility scripts

### Environment Tools (Via Symlinks)
- **JIRA**: `./tools/jira-pull` - Pull tickets and update context
- **MongoDB**: `./tools/mongo-connect` - Database connections
- **Validation**: `./tools/env-check` - Verify setup

## Project-Specific Configuration

### API Keys and Secrets
Store in `./cert/.env`:
```bash
# Project-specific API keys
PROJECT_API_KEY=xxx
PROJECT_SECRET=yyy
```

### Database Connections
Project database config in `./cert/db_config.json`

### Logging Configuration
Logs output to `./logs/` with rotation

## CRITICAL: Architectural Decision Records (ADRs)

### MANDATORY ADR Process
**BEFORE making ANY significant decision:**

1. **Read ALL existing ADRs**: `ls docs/architectural_decisions/` and review each one
2. **Check for conflicts**: Ensure new decisions don't contradict existing ADRs
3. **Document the decision**: Create new ADR using numbered format (ADR-XXX)
4. **Reference related ADRs**: Link to previous decisions that influenced this one

### When to Create ADRs
- Database schema changes
- API design decisions
- Technology stack choices
- Security implementation approaches
- Performance optimization strategies
- Integration patterns
- Deployment strategies
- ANY decision that affects future development

### ADR Template Location
Use the template in `docs/architectural_decisions/ADR-000_project_structure.md` as a guide.

## Development Guidelines

### Before Making Changes
1. **MANDATORY**: Read latest ticket: `./tools/jira-pull TICKET-XXX`
2. **MANDATORY**: Review `./docs/ARCHITECTURE.md` for current system state
3. **MANDATORY**: Check ALL ADRs in `./docs/architectural_decisions/` - understand existing decisions
4. **MANDATORY**: Verify your changes align with documented architecture decisions

### During Development
1. Keep logs in `./logs/` directory
2. Store test data in `./data/test/`
3. Add project scripts to `./scripts/`
4. **MANDATORY**: Create ADR for significant architectural decisions
5. **MANDATORY**: Update `./docs/ARCHITECTURE.md` if system structure changes

### Testing
```bash
# Run tests with project data
pytest --data-dir ./data/test

# Check logs
tail -f ./logs/app.log
```

## Current Work Items

- [ ] TICKET-XXX: {{TICKET_SUMMARY}}

## Quick Commands

```bash
# Pull latest JIRA ticket
./tools/jira-pull TICKET-XXX

# Run project scripts
./scripts/build.sh
./scripts/test.sh
./scripts/deploy.sh

# Check project logs
tail -f ./logs/development.log

# Connect to project database
./tools/mongo-connect --config ./cert/db_config.json
```

## Important Notes

1. **Self-Containment**: This project runs independently without parent directory access
2. **Local First**: Always use project-level resources before environment-level
3. **Tool Access**: Environment tools available via `./tools/` symlinks
4. **No Parent Paths**: Never use `../` in code or scripts

## Claude Code Behavior Requirements

### ADR Enforcement
Claude MUST enforce ADR documentation by:

1. **Refusing to implement architectural changes** without creating corresponding ADRs
2. **Asking for ADR creation** when detecting architectural decisions in conversation
3. **Reading existing ADRs** before proposing solutions that might conflict
4. **Suggesting ADR updates** when implementation reveals new considerations

### Working Directory Awareness
When `pwd` shows `/workspace/src/active-project/`, Claude MUST:

1. **Reference this CLAUDE.md** for project-specific context
2. **Use relative paths** (./cert/, ./data/, ./logs/) not absolute paths
3. **Check project documentation** before making assumptions
4. **Maintain project isolation** - no access to parent directories

### Documentation Maintenance
Claude MUST proactively:

1. **Update docs/ARCHITECTURE.md** when system structure changes
2. **Create numbered ADRs** for all architectural decisions
3. **Reference existing ADRs** when building on previous decisions
4. **Keep JIRA ticket context** current with `./tools/jira-pull`

## Project-Specific Rules

{{PROJECT_SPECIFIC_RULES}}