"""多智能体编排器"""

from typing import Any, Dict, List, Optional
from .workflow import Workflow, WorkflowStage
from .agent_base import AgentBase


class Orchestrator:
    def __init__(self):
        self.agents: Dict[str, AgentBase] = {}
        self.workflow: Optional[Workflow] = None
        self.global_context: Dict[str, Any] = {}

    def register_agent(self, agent: AgentBase, stage: WorkflowStage):
        self.agents[stage.value] = agent

    def set_workflow(self, workflow: Workflow):
        self.workflow = workflow

    def set_context(self, key: str, value: Any):
        self.global_context[key] = value

    async def run(self, initial_input: Any) -> Dict[str, Any]:
        if not self.workflow:
            raise RuntimeError("工作流未设置")
        print("[Orchestrator] 开始执行标书生成工作流...")
        workflow_input = initial_input
        while not self.workflow.is_complete:
            stage = self.workflow.current_stage
            agent = self.agents.get(stage.value)
            if agent:
                print(f"  → [{stage.value}] — {agent.name}")
                for k, v in self.global_context.items():
                    agent.set_context(k, v)
                result = agent.execute(workflow_input)
                self.workflow.record_result(stage, result)
                workflow_input = result
            else:
                print(f"  → [{stage.value}] — 跳过（无 Agent）")
            self.workflow.advance()
        print("[Orchestrator] 工作流执行完成")
        return self.workflow.results
