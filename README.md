# Kimi API 🌙

[![PyPI](https://img.shields.io/pypi/v/kimik2?style=flat-square)](https://pypi.org/project/kimik2/)
[![Python](https://img.shields.io/pypi/pyversions/kimik2?style=flat-square)](https://pypi.org/project/kimik2/)
[![CI](https://img.shields.io/github/workflow/status/WhiteYUNZHIstar/kimik2/ci?style=flat-square)](https://github.com/WhiteYUNZHIstar/kimik2/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/WhiteYUNZHIstar/kimik2?style=flat-square)](LICENSE)

**Kimi API** 是一个轻量级的全能工具库，支持同步/异步操作、工具调用、部分请求以及文件操作，旨在为开发者提供便捷的 API 使用体验。

## 安装

### 使用 `pip` 安装

要快速安装 `kimik2` 库，只需运行以下命令：

pip install kimik2

shell
复制代码

## 快速开始

以下是几个常见的示例，展示了如何使用 `kimik2` 库实现简单的对话、工具调用、文件处理等功能。

### 1. 简单问答

import kimik2 as kk

设置 API 密钥
kk.api_key = "sk-xxx"

创建客户端
client = kk.Client()

发起简单问答
response = client.chat("Python 为什么叫 Python?")
print(response)

shell
复制代码

### 2. 函数调用

通过工具函数调用可以扩展 API 的功能：

@kk.tool
def get_weather(city: str) -> str:
return f"{city} 今天 25°C 晴"

response = client.chat("北京天气？", tools=True)
print(response)

shell
复制代码

### 3. 文件摘要

上传文件并获取文件摘要：

file_id = kk.upload_file("paper.pdf")
msg = kk.file_msg(file_id, "用三句话总结")
response = client.chat(msg)
print(response)

shell
复制代码

### 4. 流式输出

支持实时流式输出，适用于长时间运行的任务或生成内容：

response = client.chat("讲个故事", stream=True)
for chunk in response:
print(chunk, end="")

shell
复制代码

### 5. 异步操作

支持异步调用，适合高并发场景：

import asyncio

async def async_chat():
response = await kk.Client().achat("你好")
print(response)

执行异步任务
asyncio.run(async_chat())

python
复制代码

## 功能速览

| 功能           | 示例代码                                   |
|----------------|--------------------------------------------|
| 纯文本对话     | `kk.Client().chat("你好")`                 |
| 函数调用       | `kk.Client().chat("天气", tools=True)`     |
| 续写 / JSON-Mode | `kk.partial_continue(..., prefix="{\"a\":")` |
| 文件摘要       | `kk.upload_file("paper.pdf") → 摘要`       |
| 流式输出       | `kk.Client().chat("讲个故事", stream=True)` |
| 异步调用       | `await kk.Client().achat("hi")`           |

## 开发者指南

### 克隆并运行项目

1. 克隆仓库：

git clone https://github.com/WhiteYUNZHIstar/kimik2.git
cd kimik2

markdown
复制代码

2. 创建虚拟环境并激活：

python -m venv .venv
.venv\Scripts\activate # Windows
source .venv/bin/activate # macOS / Linux

markdown
复制代码

3. 安装开发依赖（包括 `pytest` 和 `black`）：

pip install -e .[dev]

markdown
复制代码

4. 运行测试：

pytest

markdown
复制代码

### 贡献

我们欢迎任何形式的贡献！如果你有任何建议或修改，可以通过 Pull Request 进行贡献。

1. Fork 仓库并创建新的分支。
2. 提交你的修改并创建 Pull Request。
3. 在 CI 流水线通过所有测试后，我们会合并你的修改。

### 开源协议

此项目使用 MIT 许可证，详情请参阅 [LICENSE](LICENSE) 文件。
