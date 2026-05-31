"""需求分析 Agent 测试"""
from src.pits.agents.requirement import RequirementAgent

def test_requirement_agent_creation():
    agent = RequirementAgent()
    assert agent.name == "需求分析Agent"
    assert agent.description != ""

def test_requirement_agent_execute():
    agent = RequirementAgent()
    result = agent.execute("某项目招标公告...")
    assert "project_name" in result
    assert "qualification_requirements" in result
