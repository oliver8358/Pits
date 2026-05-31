"""内容撰写 Agent 测试"""
from src.pits.agents.writer import WriterAgent

def test_writer_agent_creation():
    agent = WriterAgent()
    assert agent.name == "内容撰写Agent"

def test_writer_agent_execute():
    agent = WriterAgent()
    result = agent.execute({"project_name": "测试项目"})
    assert "technical_scheme" in result
