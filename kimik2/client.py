import os, openai, asyncio
from typing import List, Dict, Any, Optional

class Client:
    def __init__(self, api_key: str = None, base_url: str = "https://api.moonshot.cn/v1"):
        self.key = api_key or __import__("kimik2").api_key or os.getenv("KIMI_API_KEY")
        if not self.key:
            raise RuntimeError("请设置 KIMI_API_KEY 环境变量或 kimik2.api_key = ...")
        self.cli = openai.OpenAI(api_key=self.key, base_url=base_url)

    def chat(self, prompt: str, model: str = "moonshot-v1-8k", **kw) -> str:
        msgs = [{"role": "user", "content": prompt}]
        resp = self.cli.chat.completions.create(model=model, messages=msgs, **kw)
        return resp.choices[0].message.content

    async def achat(self, prompt: str, model: str = "moonshot-v1-8k", **kw) -> str:
        msgs = [{"role": "user", "content": prompt}]
        loop = asyncio.get_running_loop()
        resp = await loop.run_in_executor(
            None,
            lambda: self.cli.chat.completions.create(model=model, messages=msgs, **kw)
        )
        return resp.choices[0].message.content
