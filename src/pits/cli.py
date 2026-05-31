"""Pits CLI 入口 — 交互式智能标书生成命令行工具"""

import argparse
import sys
from pathlib import Path

from .config import load_config


def main():
    parser = argparse.ArgumentParser(
        description="Pits — 智能标书生成系统",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("-i", "--input", type=str, help="招标文件路径（PDF/Word/文本）")
    parser.add_argument("--interactive", action="store_true", help="以交互式问答模式生成标书")
    parser.add_argument("--list-templates", action="store_true", help="列出所有可用标书模板")
    parser.add_argument("--config", type=str, default=None, help="指定配置文件路径")
    parser.add_argument("-o", "--output", type=str, default=None, help="输出文件路径")
    parser.add_argument("--format", choices=["docx", "pdf"], default="docx", help="输出格式")

    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    config = load_config(args.config)
    print("Pits — 智能标书生成系统")

    if args.list_templates:
        return
    if args.interactive:
        print("[交互模式] 生成引擎待实现")
        return
    if args.input:
        print(f"[✓] 正在解析: {args.input}")
        print("[!] 生成引擎待实现")


if __name__ == "__main__":
    main()
