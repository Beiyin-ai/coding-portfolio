### ~/Downloads/ai/a6/mcp_cam.g1.py'
~/v6👉 uv run '/home/nob/文件/lesson/ai_程式設計班/a6/mcp_cam.g1.py'

firefox 'http://localhost:8818/mymcp_cam.mjpg' &

/home/nob/文件/lesson/ai_程式設計班/a5/req_remote_mcp.0.sh  'http://127.0.0.1:8808/mcp'

(v6) ~/v6👉 uv run /home/nob/文件/lesson/ai_程式設計班/a6/client_http_mcp.py -a 'http://127.0.0.1:8808/sse' 
🚩tools━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩

name='get_frame' title=None description='獲取 USB 攝影機的最新畫面。\n回傳：Base64 編碼的 JPEG 圖片 (Data URI 格式字串)' inputSchema={'additionalProperties': False, 'properties': {}, 'type': 'object'} outputSchema={'properties': {'result': {'type': 'string'}}, 'required': ['result'], 'type': 'object', 'x-fastmcp-wrap-result': True} icons=None annotations=None meta={'fastmcp': {'tags': []}} execution=None 

🚩tools━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩

(v6) ~/v6👉 uv run /home/nob/文件/lesson/ai_程式設計班/a6/use_mcp_tool.py -a 'http://127.0.0.1:8808/sse' -t "get_frame" -p '{}'

🚩result━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩

CallToolResult(content=[TextContent(type='text', text='data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAIBAQEBAQIBAQECAgICAgQDAgICAgUEBAMEBgUGBgYFBgYGBwkIBgcJBwYGCAsICQoKCgoKBggLDAsKDAkKCgr/
................................
.................................... 

🚩result━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩

https://gemini.google.com/share/23410b250d9a