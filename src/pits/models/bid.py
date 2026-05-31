"""标书数据模型"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class BidDocument:
    title: str = ""
    project_name: str = ""
    bidder_name: str = ""
    sections: Dict[str, str] = field(default_factory=dict)
    attachments: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: str = ""
    version: str = "0.1.0"
    compliance_report: Optional[dict] = None


@dataclass
class Chapter:
    title: str
    content: str
    order: int = 0
    required: bool = True
    word_count: int = 0
