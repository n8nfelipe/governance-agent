#!/usr/bin/env bash
set -euo pipefail

AGENTS_DIR="${HOME}/.config/opencode/agents"
SRC="$(cd "$(dirname "$0")" && pwd)/governance-agent.md"

if [ ! -f "$SRC" ]; then
    echo "❌ governance-agent.md not found alongside this script"
    exit 1
fi

mkdir -p "$AGENTS_DIR"
cp "$SRC" "$AGENTS_DIR/governance-agent.md"

echo "✅ Installed governance-agent.md → ${AGENTS_DIR}/"
echo "   Available at: ${AGENTS_DIR}/governance-agent.md"
