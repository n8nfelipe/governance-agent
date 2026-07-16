# governance-agent

OpenCode agent for software governance audits — licenses, dependencies, code standards, security, and architecture.

## Features

| Domain | What it checks |
|--------|----------------|
| **Licenses** | Compatibility, missing LICENSE file, unlicensed deps |
| **Dependencies** | Outdated, deprecated, duplicates, lockfiles |
| **Code Standards** | Linter, formatting, type hints, dead code |
| **Security** | Secrets leaked, `.env` in `.gitignore`, CVEs, unsafe patterns |
| **Architecture** | SRP, file size, coupling, directory structure, test coverage |

## Installation

```bash
# Clone the repo
git clone https://github.com/n8nfelipe/governance-agent.git
cd governance-agent

# Install the agent for OpenCode
./install.sh
```

Or manually:
```bash
cp governance-agent.md ~/.config/opencode/agents/
```

## Usage

In OpenCode, use the `task` tool to delegate:

> "roda o governance-agent no projeto X"
> "audita esse repositório"
> "faz uma análise de governança no diretório Y"

The agent will analyze 5 domains and produce a report with:
- Executive summary (✅ / ⚠️ / ❌ per domain)
- Detailed findings with file:line evidence
- Prioritized recommendations (Must fix / Should fix / Nice to have)

## Development

```bash
pip install -e ".[test]"
pytest -v
```

## Requirements

- OpenCode with `task` tool support
- `bash`, `read`, `webfetch`, `websearch` permissions (configured in the agent)
