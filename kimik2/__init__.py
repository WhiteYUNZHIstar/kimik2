"""kimik2 — Kimi API 超轻全家桶"""
__version__ = "0.1.0"

from .client import Client
from . import file, token, tool, constants

# 快捷导出
api_key = None
MODEL_8K   = "moonshot-v1-8k"
MODEL_32K  = "moonshot-v1-32k"
MODEL_128K = "moonshot-v1-128k"
MODEL_K2_THINKING = "moonshot-k2-thinking"
