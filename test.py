import os, sys
from dotenv import load_dotenv

load_dotenv()

from src.agent.graph import run_agent

result = run_agent(
    "Tạo đơn hàng cho Nguyễn Lan Anh, số điện thoại 0901234567, email lananh@example.com...",
    provider="openclaude",
)
print(result.final_answer)
print(result.tool_calls)