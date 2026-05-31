"""LLM 推理封装"""

from typing import Any, Dict, List, Optional


class LLMClient:
    def __init__(self, config: dict):
        self.provider = config.get("provider", "openai")
        self.api_key = config.get("api_key", "")
        self.model = config.get("model", "gpt-4")
        self.base_url = config.get("base_url", "")

    async def chat(self, messages: List[dict], **kwargs) -> str:
        print(f"    [LLM] 调用 {self.provider}/{self.model}")
        return ""

    async def stream_chat(self, messages: List[dict], **kwargs):
        yield ""
