# Para usar o governance-agent no Claude Code
#
# Adicione o conteúdo abaixo no arquivo CLAUDE.md do seu projeto
# (https://docs.anthropic.com/en/docs/claude-code/overview)
#
# Quando quiser rodar uma auditoria, diga algo como:
# "roda o governance-agent no projeto" ou "audita esse repositório"

---
Referência: https://github.com/n8nfelipe/governance-agent
---

## Governance Agent

Quando solicitado a auditar a governança de software deste projeto, analise os 5 domínios abaixo e produza um relatório com:
- Resumo executivo (✅ / ⚠️ / ❌ por domínio)
- Achados detalhados com arquivo:linha
- Recomendações priorizadas (Must fix / Should fix / Nice to have)

### Domínios

1. **Licenças** — compatibilidade, arquivo LICENSE, deps sem licença
2. **Dependências** — desatualizadas, deprecated, duplicadas, lockfiles
3. **Padrões de Código** — linter, formatação, type hints, código morto
4. **Segurança** — secrets vazados, .env no .gitignore, CVEs, práticas inseguras
5. **Arquitetura** — SRP, tamanho de arquivos, acoplamento, estrutura, testes

### Workflow

1. Leia arquivos-chave (package.json, pyproject.toml, tsconfig.json, .github/workflows, .gitignore, LICENSE etc.)
2. Explore a estrutura do projeto
3. Execute ferramentas disponíveis (linters, audit, typecheck)
4. Analise cada domínio criticamente
5. Produza relatório com evidências específicas
