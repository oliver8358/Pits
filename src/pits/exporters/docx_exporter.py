"""Word 文档导出器"""

from pathlib import Path
from typing import Any, Dict, Optional


class DocxExporter:
    def __init__(self):
        self.document = None

    def export(self, content: Dict[str, Any], output_path: str, template_path: Optional[str] = None):
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        print(f"    [DocxExporter] 正在生成 Word 文档: {output_path}")
