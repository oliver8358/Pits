"""Pits 配置管理模块"""

import os
from pathlib import Path
from typing import Dict, Optional

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = lambda path: None


DEFAULT_CONFIG = {
    "LLM_PROVIDER": "openai",
    "LLM_API_KEY": "",
    "LLM_MODEL": "gpt-4",
    "LLM_BASE_URL": "",
    "VECTOR_STORE_PATH": "./data/vector_store",
    "TEMPLATE_DIR": "./templates",
    "OUTPUT_DIR": "./output",
    "LOG_LEVEL": "INFO",
}


def load_config(config_path: Optional[str] = None) -> Dict[str, str]:
    if config_path:
        env_file = Path(config_path)
    else:
        env_file = Path.cwd() / ".env"
    if env_file.exists():
        load_dotenv(env_file)
    config = DEFAULT_CONFIG.copy()
    for key in config:
        env_val = os.environ.get(key)
        if env_val is not None:
            config[key] = env_val
    return config


def get_llm_config(config: Dict[str, str]) -> dict:
    return {
        "provider": config["LLM_PROVIDER"],
        "api_key": config["LLM_API_KEY"],
        "model": config["LLM_MODEL"],
        "base_url": config["LLM_BASE_URL"],
    }
