"""模板引擎测试"""
from src.pits.capabilities.template import TemplateEngine

def test_template_engine_init():
    engine = TemplateEngine("/nonexistent")
    assert engine.template_dir.name == "nonexistent"
