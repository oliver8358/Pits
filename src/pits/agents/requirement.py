"""需求分析 Agent"""

from ..core.agent_base import AgentBase


class RequirementAgent(AgentBase):
    """需求分析智能体：解析招标文件，提取关键字段"""

    def __init__(self):
        super().__init__(
            name="需求分析Agent",
            description="解析招标文件，提取项目名称、预算、资质要求、评分标准等",
        )

    def execute(self, input_data: str, **kwargs) -> dict:
        print(f"    [{self.name}] 正在解析招标需求...")
        result = {
            "project_name": "",
            "budget": "",
            "qualification_requirements": [],
            "technical_requirements": [],
            "evaluation_criteria": [],
            "deadline": "",
            "raw_text": input_data,
        }
        return result
