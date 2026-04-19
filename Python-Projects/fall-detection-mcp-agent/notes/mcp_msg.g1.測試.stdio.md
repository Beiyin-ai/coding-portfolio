(v6) ~/v6👉 uv run '/home/nob/文件/lesson/ai_程式設計班/a6/mcp_msg.g1.py' 

╭──────────────────────────────────────────────────────────────────────────────╮                                                 
│                                                 
│                                FastMCP 3.1.0                                 │                                                 
│                            https://gofastmcp.com                             │                                                 
│                                                                              │                                                 
│                    🖥  Server:      MonitorServer, 3.1.0                      │                                                 
│                    🚀 Deploy free: https://fastmcp.cloud                     │                                                 
│                                                                              │                                                 
╰──────────────────────────────────────────────────────────────────────────────╯                                                 

### 🥁 在另一終端機 跑 ⤵      🥁
👉 firefox --window-size 640,320  --new-window 'http://localhost:8817/' &

### 🥁 回到原本跑 MCP 伺服器的 終端機      🥁
### 🥁 貼上 ⤵      🥁
{"jsonrpc":"2.0","method":"notifications/initialized"}
{"jsonrpc":"2.0","method":"tools/list","id":1}

# 🥁 會跑出 ⤵      🥁

{"jsonrpc":"2.0","id":1,"result":{"tools":[{"name":"send_log_to_web","description":"將訊息傳送並顯示在 port 8817 的監控網頁上。\n這對於 Agent 輸出思考過程、除錯資訊或狀態回報非常有用。","inputSchema":{"additionalProperties":false,"properties":{"message":{"type":"string"}},"required":["message"],"type":"object"},"outputSchema":{"properties":{"result":{"type":"string"}},"required":["result"],"type":"object","x-fastmcp-wrap-result":true},"_meta":{"fastmcp":{"tags":[]}}}]}}


### 🥁 一列一列分別貼上 ⤵      🥁 貼上之後觀察 firefox 瀏覽器 localhost:8817 網頁

{"jsonrpc":"2.0","method":"tools/call","id":101, "params": {"name":"send_log_to_web", "arguments": {"message":"📢 測試！測試！人工輸入" }}}
{"jsonrpc":"2.0","method":"tools/call","id":757, "params": {"name":"send_log_to_web", "arguments": {"message":"💥 test test 💥" }}}
{"jsonrpc":"2.0","method":"tools/call","id":757, "params": {"name":"send_log_to_web", "arguments": {"message":"🔔 手打的 手打的 🔔" }}}