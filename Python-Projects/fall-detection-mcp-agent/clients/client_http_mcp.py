# uv run 您的檔案路徑/client_http_mcp.py -a "http://127.0.0.1:8801/mcp"
# uv run 您的檔案路徑/client_http_mcp.py -a "https://gofastmcp.com/mcp"
# uv run 您的檔案路徑/client_http_mcp.py -a "https://mcp.deepwiki.com/mcp"

import asyncio
from fastmcp import Client
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--address', default='https://mcp.deepwiki.com/mcp', help='MCP server addr')
args = parser.parse_args()

client = Client(args.address)

async def main():
    async with client:
        tools = await client.list_tools()
        print('🚩tools━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩\n')
        for i in tools:
            print(i, '\n')
        print('🚩tools━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩\n')

asyncio.run(main())
