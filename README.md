# governance-agent

Agent de auditoria de governança de software para ferramentas de IA — analisa licenças, dependências, padrões de código, segurança e arquitetura.

## Suporte por Ferramenta

| Ferramenta | Como instalar | Arquivo de referência |
|------------|--------------|----------------------|
| **OpenCode** | `cp governance-agent.md ~/.config/opencode/agents/` | [`configs/opencode.jsonc`](configs/opencode.jsonc) |
| **Claude Code** | Adicionar em `CLAUDE.md` do projeto | [`configs/claude-code.md`](configs/claude-code.md) |
| **Cursor** | Criar `.cursor/rules/governance-agent.mdc` | [`configs/cursor.md`](configs/cursor.md) |
| **GitHub Copilot** | Adicionar em `.github/copilot-instructions.md` | [`configs/copilot.md`](configs/copilot.md) |
| **Continue.dev** | Adicionar rule em `~/.continue/config.json` | [`configs/continue.md`](configs/continue.md) |
| **Genérico** | Usar `SYSTEM_PROMPT.md` como instrução de sistema | [`SYSTEM_PROMPT.md`](SYSTEM_PROMPT.md) |

## Domínios de Auditoria

| Domínio | O que verifica |
|---------|----------------|
| **Licenças** | Compatibilidade, arquivo LICENSE ausente, deps sem licença |
| **Dependências** | Desatualizadas, deprecated, duplicadas, lockfiles |
| **Padrões de Código** | Linter, formatação, type hints, código morto |
| **Segurança** | Secrets vazados, `.env` no `.gitignore`, CVEs, práticas inseguras |
| **Arquitetura** | SRP, tamanho de arquivos, acoplamento, estrutura, testabilidade |

## Formato do Relatório

Toda auditoria produz:
- **Resumo executivo** — nota por domínio (✅ / ⚠️ / ❌)
- **Achados detalhados** — evidências com arquivo:linha
- **Recomendações priorizadas** — Must fix / Should fix / Nice to have

## Estrutura do Projeto

```
├── governance-agent.md        # Agent file (OpenCode)
├── SYSTEM_PROMPT.md           # Prompt genérico (qualquer ferramenta)
├── configs/
│   ├── opencode.jsonc
│   ├── claude-code.md
│   ├── cursor.md
│   ├── copilot.md
│   └── continue.md
├── install.sh                 # Instalação via OpenCode
├── src/validate_agent.py      # Validador do arquivo de agente
├── tests/                     # Testes (pytest)
├── .github/workflows/ci.yml   # CI + release automática
└── pyproject.toml
```

## Desenvolvimento

```bash
pip install -e ".[test]"
pytest -v
```
