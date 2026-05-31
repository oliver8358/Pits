"""PDF 导出器"""

from pathlib import Path
from typing import Any, Dict, Optional


class PdfExporter:
    def __init__(self):
        pass

    def export(self, content: Dict[str, Any], output_path: str):
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        print(f"    [PdfExporter] 正在生成 PDF 文档: {output_path}")
