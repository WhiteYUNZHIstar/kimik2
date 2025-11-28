# Kimi API 🌙

[![PyPI](https://img.shields.io/pypi/v/kimik2?style=flat-square)](https://pypi.org/project/kimik2/)
[![Python](https://img.shields.io/pypi/pyversions/kimik2?style=flat-square)](https://pypi.org/project/kimik2/)
[![CI](https://img.shields.io/github/actions/workflow/status/WhiteYUNZHIstar/kimik2/ci.yml?style=flat-square)](https://github.com/WhiteYUNZHIstar/kimik2/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/WhiteYUNZHIstar/kimik2?style=flat-square)](LICENSE)

**Kimi API** 是一个轻量级全能工具库，支持同步/异步、工具调用、部分请求、文件操作，让开发者 3 行代码就能用上 Kimi 大模型。

## 安装
```bash
pip install kimik2
快速开始（3 行运行）
Python
复制
import kimik2 as kk
kk.api_key = "sk-xxx"          # 换成你的真实 Key
print(kk.Client().chat("1+1=? 只给数字"))
能力一览
表格
复制
场景	代码片段
纯文本问答	kk.Client().chat("你好")
函数调用	kk.Client().chat("北京天气？", tools=True)
续写 / JSON-Mode	kk.partial_continue(..., prefix="{\"a\":")
文件摘要	kk.upload_file("paper.pdf") → 摘要
流式输出	kk.Client().chat("讲个故事", stream=True)
异步高并发	await kk.Client().achat("hi")
示例合集
① 函数调用
Python
复制
@kk.tool
def get_weather(city: str) -> str:
    return f"{city} 今天 25°C 晴"

client = kk.Client()
print(client.chat("北京天气？", tools=True))
② 文件摘要
Python
复制
file_id = kk.upload_file("paper.pdf")
msg = kk.file_msg(file_id, "用三句话总结")
print(client.chat(msg))
③ 流式输出
Python
复制
for chunk in client.chat("讲个故事", stream=True):
    print(chunk, end="")
④ 异步调用
Python
复制
import asyncio
async def main():
    print(await kk.Client().achat("你好"))
asyncio.run(main())
开发指南
bash
复制
git clone https://github.com/WhiteYUNZHIstar/kimik2.git
cd kimik2
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS/Linux
pip install -e .[dev]           # 含 pytest、black
pytest                          # 跑测试
贡献 & 协议
欢迎 PR / Issue！仓库使用 MIT 协议。
复制

--------------------------------
一键覆盖
--------------------------------
PowerShell 一句：

```powershell
Set-Content -Path "C:\Users\Administrator\Desktop\kimik2\kimik2\README.md" -Value @"
# Kimi API 🌙

[![PyPI](https://img.shields.io/pypi/v/kimik2?style=flat-square)](https://pypi.org/project/kimik2/)
[![Python](https://img.shields.io/pypi/pyversions/kimik2?style=flat-square)](https://pypi.org/project/kimik2/)
[![CI](https://img.shields.io/github/actions/workflow/status/WhiteYUNZHIstar/kimik2/ci.yml?style=flat-square)](https://github.com/WhiteYUNZHIstar/kimik2/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/WhiteYUNZHIstar/kimik2?style=flat-square)](LICENSE)

**Kimi API** 是一个轻量级全能工具库，支持同步/异步、工具调用、部分请求、文件操作，让开发者 3 行代码就能用上 Kimi 大模型。

## 安装
```bash
pip install kimik2
快速开始（3 行运行）
Python
复制
import kimik2 as kk
kk.api_key = "sk-xxx"          # 换成你的真实 Key
print(kk.Client().chat("1+1=? 只给数字"))
能力一览
表格
复制
场景	代码片段
纯文本问答	kk.Client().chat("你好")
函数调用	kk.Client().chat("北京天气？", tools=True)
续写 / JSON-Mode	kk.partial_continue(..., prefix="{\"a\":")
文件摘要	kk.upload_file("paper.pdf") → 摘要
流式输出	kk.Client().chat("讲个故事", stream=True)
异步高并发	await kk.Client().achat("hi")
示例合集
① 函数调用
Python
复制
@kk.tool
def get_weather(city: str) -> str:
    return f"{city} 今天 25°C 晴"

client = kk.Client()
print(client.chat("北京天气？", tools=True))
② 文件摘要
Python
复制
file_id = kk.upload_file("paper.pdf")
msg = kk.file_msg(file_id, "用三句话总结")
print(client.chat(msg))
③ 流式输出
Python
复制
for chunk in client.chat("讲个故事", stream=True):
    print(chunk, end="")
④ 异步调用
Python
复制
import asyncio
async def main():
    print(await kk.Client().achat("你好"))
asyncio.run(main())
开发指南
bash
复制
git clone https://github.com/WhiteYUNZHIstar/kimik2.git
cd kimik2
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS/Linux
pip install -e .[dev]           # 含 pytest、black
pytest                          # 跑测试
贡献 & 协议
欢迎 PR / Issue！仓库使用 MIT 协议。
"@ -Encoding utf8
