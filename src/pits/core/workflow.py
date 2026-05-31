"""工作流定义"""

from enum import Enum
from typing import List, Dict, Any, Optional


class WorkflowStage(Enum):
    REQUIREMENT_ANALYSIS = "需求分析"
    TECHNICAL_SCHEME = "技术方案撰写"
    BUSINESS_QUOTATION = "商务报价"
    PROJECT_MANAGEMENT = "项目管理"
    COMPLIANCE_CHECK = "合规审查"
    FORMAT_REVIEW = "格式编排"
    QUALITY_INSPECTION = "质量终检"
    EXPORT = "导出输出"


class Workflow:
    DEFAULT_FLOW = [
        WorkflowStage.REQUIREMENT_ANALYSIS,
        WorkflowStage.TECHNICAL_SCHEME,
        WorkflowStage.BUSINESS_QUOTATION,
        WorkflowStage.PROJECT_MANAGEMENT,
        WorkflowStage.COMPLIANCE_CHECK,
        WorkflowStage.FORMAT_REVIEW,
        WorkflowStage.QUALITY_INSPECTION,
        WorkflowStage.EXPORT,
    ]

    def __init__(self, stages: Optional[List[WorkflowStage]] = None):
        self.stages = stages or self.DEFAULT_FLOW.copy()
        self.current_index: int = 0
        self.results: Dict[str, Any] = {}

    @property
    def current_stage(self) -> Optional[WorkflowStage]:
        if self.current_index < len(self.stages):
            return self.stages[self.current_index]
        return None

    @property
    def is_complete(self) -> bool:
        return self.current_index >= len(self.stages)

    def advance(self) -> bool:
        if self.is_complete:
            return False
        self.current_index += 1
        return True

    def record_result(self, stage: WorkflowStage, result: Any):
        self.results[stage.value] = result
