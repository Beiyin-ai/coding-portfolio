# uv run 您的檔案路徑/use_mcp_tool.py -a "http://127.0.0.1:8801/mcp" -t "multiply" -p "{\"a\": 5, \"b\": 3}"
# uv run 您的檔案路徑/use_mcp_tool.py -a "https://mcp.deepwiki.com/mcp" -t "ask_question" -p "{\"repoName\":\"ggml-org/llama.cpp\",\"question\":\"這個專案的主要用途是什麼？\"}"

import asyncio
from fastmcp import Client
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--address', default='https://mcp.deepwiki.com/mcp', help='MCP server addr')
parser.add_argument('-t', '--tool', default='read_wiki_structure', help='MCP tool name')
parser.add_argument('-p', '--param', default='{"repoName": "huggingface/transformers"}', help='MCP tool parameters')
args = parser.parse_args()

client = Client(args.address)

async def use_mcp_tool():
    async with client:
        para_obj = json.loads(args.param)
        result = await client.call_tool(args.tool, para_obj)
        print('🚩result━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩\n')
        print(result, "\n")
        print('🚩result━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩\n')

asyncio.run(use_mcp_tool())
