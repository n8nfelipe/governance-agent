from pathlib import Path

import yaml

AGENTS_DIR = Path.home() / ".config" / "opencode" / "agents"
PERMISSIONS = {"read", "edit", "write", "bash", "webfetch", "websearch"}
PERM_VALUES = {"allow", "deny"}
VALID_MODES = {"subagent", "chat"}


class AgentValidationError(Exception):
    pass


def validate_frontmatter(content: str) -> dict:
    if not content.startswith("---"):
        raise AgentValidationError("Frontmatter must start with `---`")

    parts = content.split("---", 2)
    if len(parts) < 3:
        raise AgentValidationError("Frontmatter not properly closed with `---`")

    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        raise AgentValidationError(f"Invalid YAML in frontmatter: {e}")

    if not isinstance(meta, dict):
        raise AgentValidationError("Frontmatter must be a YAML dictionary")

    if "description" not in meta or not isinstance(meta["description"], str):
        raise AgentValidationError("Missing or invalid `description` field")

    if "mode" not in meta or meta["mode"] not in VALID_MODES:
        raise AgentValidationError(f"Invalid `mode`: must be one of {VALID_MODES}")

    if "temperature" in meta:
        temp = meta["temperature"]
        if not isinstance(temp, (int, float)) or temp < 0 or temp > 1:
            raise AgentValidationError("`temperature` must be between 0 and 1")

    if "permission" in meta:
        perms = meta["permission"]
        if not isinstance(perms, dict):
            raise AgentValidationError("`permission` must be a dictionary")
        for key, val in perms.items():
            if key not in PERMISSIONS:
                raise AgentValidationError(f"Unknown permission: `{key}`")
            if val not in PERM_VALUES:
                raise AgentValidationError(f"Permission `{key}` must be 'allow' or 'deny'")

    return meta


def validate_agent_file(filepath: Path) -> dict:
    content = filepath.read_text(encoding="utf-8")
    return validate_frontmatter(content)


def main():
    agent_file = Path(__file__).parent.parent / "governance-agent.md"
    if not agent_file.exists():
        print(f"Agent file not found: {agent_file}")
        return 1

    try:
        meta = validate_agent_file(agent_file)
        print(f"✅ {agent_file.name} — valid")
        print(f"   Description: {meta['description']}")
        print(f"   Mode: {meta['mode']}")
        print(f"   Temperature: {meta.get('temperature', 'N/A')}")
        return 0
    except AgentValidationError as e:
        print(f"❌ {agent_file.name} — {e}")
        return 1


if __name__ == "__main__":
    exit(main())
