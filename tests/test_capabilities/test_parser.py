"""文档解析能力测试"""
from pathlib import Path
import tempfile
from src.pits.capabilities.parser import DocumentParser

def test_parser_supported_extensions():
    parser = DocumentParser()
    assert ".pdf" in parser.SUPPORTED_EXTENSIONS
    assert ".docx" in parser.SUPPORTED_EXTENSIONS
    assert ".txt" in parser.SUPPORTED_EXTENSIONS

def test_parser_txt_file():
    parser = DocumentParser()
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("招标文件测试内容")
        tmp_path = f.name
    try:
        result = parser.parse(tmp_path)
        assert "招标文件测试内容" in result
    finally:
        Path(tmp_path).unlink()
