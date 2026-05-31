"""模板引擎"""

from pathlib import Path
from typing import Any, Dict, Optional

try:
    from jinja2 import Environment, FileSystemLoader, TemplateNotFound
except ImportError:
    Environment = None
    FileSystemLoader = None
    TemplateNotFound = Exception


class TemplateEngine:
    def __init__(self, template_dir: str = "./templates"):
        self.template_dir = Path(template_dir)
        self.env = None
        if Environment and self.template_dir.exists():
            self.env = Environment(
                loader=FileSystemLoader(str(self.template_dir)),
                autoescape=False,
            )

    def render(self, template_name: str, context: Dict[str, Any]) -> str:
        if not self.env:
            raise RuntimeError("Jinja2 未安装或模板目录不存在")
        try:
            template = self.env.get_template(template_name)
            return template.render(**context)
        except TemplateNotFound:
            raise FileNotFoundError(f"模板不存在: {template_name}")

    def list_templates(self) -> list:
        if not self.template_dir.exists():
            return []
        return [f.name for f in self.template_dir.iterdir() if f.is_file()]
