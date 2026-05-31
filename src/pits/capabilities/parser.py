"""文档解析能力"""

from pathlib import Path
from typing import Optional


class DocumentParser:
    SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".doc", ".txt", ".md"}

    def __init__(self):
        self.parsed_data: Optional[str] = None

    def parse(self, file_path: str) -> str:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")

        ext = path.suffix.lower()
        if ext not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(f"不支持的文件格式: {ext}")

        print(f"    [Parser] 正在解析 {ext} 文件: {path.name}")

        if ext == ".txt":
            return path.read_text(encoding="utf-8")
        elif ext == ".md":
            return path.read_text(encoding="utf-8")
        elif ext == ".pdf":
            return f"[PDF 解析待实现] {file_path}"
        elif ext in (".docx", ".doc"):
            return f"[Word 解析待实现] {file_path}"

        return ""
