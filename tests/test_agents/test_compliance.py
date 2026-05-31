"""合规审查 Agent 测试"""
from src.pits.agents.compliance import ComplianceAgent

def test_compliance_agent_creation():
    agent = ComplianceAgent()
    assert agent.name == "合规审查Agent"

def test_compliance_agent_execute():
    agent = ComplianceAgent()
    result = agent.execute({"technical_scheme": "..."})
    assert "compliance_score" in result
    assert "issues" in result
