#!/usr/bin/env bash
set -euo pipefail

SRC="$(cd "$(dirname "$0")" && pwd)"

install_opencode() {
  AGENTS_DIR="${HOME}/.config/opencode/agents"
  SRC_FILE="${SRC}/governance-agent.md"

  if [ ! -f "$SRC_FILE" ]; then
    echo "❌ governance-agent.md not found alongside this script"
    exit 1
  fi

  mkdir -p "$AGENTS_DIR"
  cp "$SRC_FILE" "$AGENTS_DIR/governance-agent.md"

  echo "✅ Installed governance-agent.md → ${AGENTS_DIR}/"
  echo "   Available at: ${AGENTS_DIR}/governance-agent.md"
}

install_codex() {
  CODEX_DIR="${HOME}/.codex/agents"
  SRC_FILE="${SRC}/configs/codex.toml"

  if [ ! -f "$SRC_FILE" ]; then
    echo "❌ configs/codex.toml not found"
    exit 1
  fi

  mkdir -p "$CODEX_DIR"
  cp "$SRC_FILE" "$CODEX_DIR/governance-agent.toml"

  echo "✅ Installed governance-agent → ${CODEX_DIR}/"
  echo "   Available at: ${CODEX_DIR}/governance-agent.toml"
  echo ""
  echo "   Use with: codex 'run governance-agent audit on this repo'"
}

case "${1:-}" in
  --codex)
    install_codex
    ;;
  --opencode|*)
    install_opencode
    ;;
esac
