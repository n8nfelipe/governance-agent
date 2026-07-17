# governance-agent

Agent de auditoria de governança de software para ferramentas de IA — analisa licenças, dependências, padrões de código, segurança e arquitetura.

## Uso Rápido

Para auditar qualquer projeto, basta **chamar o `governance-agent` e apontar para o diretório alvo**. Não é preciso instalar nada no projeto auditado — o agente lê a estrutura, roda as verificações e gera o relatório.

**OpenCode (slash command):**

```
/governance-agent audite o projeto em ~/infra/youtube-mcp
/governance-agent audite o projeto em . "foco em licenças e segurança"
```

**OpenCode (via CLI `governance`):**

```
./governance audit ~/infra/youtube-mcp
./governance audit . "só segurança"
```

**Codex CLI:**

```
codex --agent configs/codex.toml "audite o projeto em ~/infra/cloudflare-dns-manager"
```

**Outras ferramentas:** use o [`SYSTEM_PROMPT.md`](SYSTEM_PROMPT.md) como instrução de sistema e passe o caminho do projeto como argumento.

> O escopo (domínios) pode ser restrito numa frase, ex: `"foque em dependências e segurança"`. Se nenhum escopo for dado, o agente faz a auditoria completa.

## Suporte por Ferramenta

| Ferramenta | Como instalar | Arquivo de referência |
|------------|--------------|----------------------|
| **OpenCode** | `cp governance-agent.md ~/.config/opencode/agents/` | [`configs/opencode.jsonc`](configs/opencode.jsonc) |
| **Codex CLI** | `./install.sh --codex` ou `cp configs/codex.toml ~/.codex/agents/` | [`configs/codex.toml`](configs/codex.toml) |
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

## Uso como CLI Local

O script `governance` roda o agente em qualquer repositório via OpenCode e salva o relatório:

```bash
# Tornar executável (já está)
chmod +x governance

# Auditar repositório atual (escopo completo)
./governance audit .

# Auditar subdiretório com escopo restrito
./governance audit ./api "só segurança"

# Salvar relatório em ./governance-report.md (default)
./governance audit .

# Saída direta no terminal (sem arquivo)
./governance audit . --stdout | less -R

# Especificar modelo
./governance audit . --model openai/gpt-5

# Instalar agente no OpenCode ou Codex CLI
./governance install          # OpenCode (default)
./governance install --codex  # Codex CLI
```

Pré-requisitos: [`opencode`](https://opencode.ai) instalado e o agente `governance-agent` disponível (rode `./governance install` primeiro).

## Estrutura do Projeto

```
├── governance-agent.md        # Agent file (OpenCode)
├── governance                  # CLI local: roda auditoria em qualquer repo
├── SYSTEM_PROMPT.md           # Prompt genérico (qualquer ferramenta)
├── configs/
│   ├── opencode.jsonc
│   ├── codex.toml
│   ├── claude-code.md
│   ├── cursor.md
│   ├── copilot.md
│   └── continue.md
├── install.sh                 # Instalação via OpenCode (default) ou Codex CLI (--codex)
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
