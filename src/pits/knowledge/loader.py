"""知识加载器"""

from pathlib import Path
from typing import Any, Dict, List, Optional


class KnowledgeLoader:
    def __init__(self, base_dir: str = "./knowledge_base"):
        self.base_dir = Path(base_dir)

    def load_company_info(self) -> dict:
        info_file = self.base_dir / "company_info.json"
        if info_file.exists():
            import json
            return json.loads(info_file.read_text(encoding="utf-8"))
        return {}

    def load_project_cases(self) -> List[dict]:
        cases_file = self.base_dir / "project_cases.json"
        if cases_file.exists():
            import json
            return json.loads(cases_file.read_text(encoding="utf-8"))
        return []

    def load_certifications(self) -> List[str]:
        cert_file = self.base_dir / "certifications.json"
        if cert_file.exists():
            import json
            return json.loads(cert_file.read_text(encoding="utf-8"))
        return []
