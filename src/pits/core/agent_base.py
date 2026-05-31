"""Agent 基类"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class AgentBase(ABC):
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.context: Dict[str, Any] = {}

    @abstractmethod
    def execute(self, input_data: Any, **kwargs) -> Any:
        raise NotImplementedError

    def set_context(self, key: str, value: Any):
        self.context[key] = value

    def get_context(self, key: str, default: Any = None) -> Any:
        return self.context.get(key, default)

    def __repr__(self) -> str:
        return f"<Agent: {self.name}>"
