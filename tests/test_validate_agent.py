from pathlib import Path

import pytest

from src.validate_agent import (
    AgentValidationError,
    validate_agent_file,
    validate_frontmatter,
)


class TestValidateFrontmatter:
    def test_valid_governance_agent(self):
        filepath = Path(__file__).parent.parent / "governance-agent.md"
        meta = validate_agent_file(filepath)
        assert meta["description"] == (
            "Auditor de governança de software — licenças, "
            "dependências, padrões de código, segurança e arquitetura"
        )
        assert meta["mode"] == "subagent"
        assert meta["temperature"] == 0.1
        assert meta["permission"]["read"] == "allow"
        assert meta["permission"]["bash"] == "allow"
        assert meta["permission"]["webfetch"] == "allow"
        assert meta["permission"]["websearch"] == "allow"
        assert meta["permission"]["edit"] == "deny"
        assert meta["permission"]["write"] == "deny"

    def test_missing_description(self):
        content = "---\nmode: subagent\n---\n\nBody"
        with pytest.raises(AgentValidationError, match="description"):
            validate_frontmatter(content)

    def test_invalid_mode(self):
        content = "---\ndescription: Test\nmode: invalid\n---\n\nBody"
        with pytest.raises(AgentValidationError, match="mode"):
            validate_frontmatter(content)

    def test_invalid_temperature(self):
        content = "---\ndescription: Test\nmode: subagent\ntemperature: 1.5\n---\n\nBody"
        with pytest.raises(AgentValidationError, match="temperature"):
            validate_frontmatter(content)

    def test_unknown_permission(self):
        content = "---\ndescription: Test\nmode: subagent\npermission:\n  fly: allow\n---\n\nBody"
        with pytest.raises(AgentValidationError, match="Unknown permission"):
            validate_frontmatter(content)

    def test_no_frontmatter(self):
        with pytest.raises(AgentValidationError, match="start with"):
            validate_frontmatter("no frontmatter here")
