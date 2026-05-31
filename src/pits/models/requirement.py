"""需求数据模型"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class BidRequirement:
    project_name: str = ""
    budget: str = ""
    deadline: str = ""
    project_type: str = ""
    qualification_requirements: List[str] = field(default_factory=list)
    technical_requirements: List[str] = field(default_factory=list)
    evaluation_criteria: List[dict] = field(default_factory=list)
    submission_requirements: List[str] = field(default_factory=list)
    raw_text: str = ""
    parsed_sections: dict = field(default_factory=dict)
