# Para usar o governance-agent no Continue.dev
#
# Adicione uma regra em ~/.continue/config.json
# https://docs.continue.dev/customize/tips-and-tricks
#
# Exemplo:
# {
#   "rules": [
#     {
#       "name": "Governance Agent",
#       "description": "Software governance auditor",
#       "rule": "Quando solicitado a auditar governança..."
#     }
#   ]
# }

## Governance Audit Agent

Quando solicitado a auditar a governança de um projeto, analise 5 domínios:

1. Licenças
2. Dependências
3. Padrões de Código
4. Segurança
5. Arquitetura

Produza relatório com resumo executivo (✅/⚠️/❌), achados com evidências, e recomendações priorizadas.
