🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞 

https://gemini.google.com/share/28fad93d557e

https://chatgpt.com/share/69c80d62-f518-83e8-8adb-b6781f7480ca

🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞 

底下 URL 是驅動 sg90 servo 伺服馬達 的 IP 

uv run /home/nob/文件/lesson/ai_程式設計班/a6/client_http_mcp.py -a 'http://10.42.0.110:80/mcp'

uv run /home/nob/文件/lesson/ai_程式設計班/a6/use_mcp_tool.py -a 'http://10.42.0.110:80/mcp' -t "set_servo_angle" -p '{"angle": 90}'

🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞 

~/my-mcp👉 uv run /home/nob/文件/lesson/ai_程式設計班/a5/client_http_mcp.1.py -a 'http://10.42.0.110:80/mcp'
🚩tools━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩

name='set_servo_angle' title=None description='控制接在 GPIO4 的 SG90 伺服馬達轉動指定角度' inputSchema={'properties': {'angle': {'minimum': 0, 'type': 'integer', 'maximum': 180, 'description': '0 到 180 的整數角度'}}, 'required': ['angle'], 'type': 'object'} outputSchema=None icons=None annotations=None meta=None execution=None 

🚩tools━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩

~/my-mcp👉 uv run /home/nob/文件/lesson/ai_程式設計班/a6/use_mcp_tool.py -a 'http://10.42.0.110:80/mcp' -t "set_servo_angle" -p '{"angle": 0}'
🚩result━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩

CallToolResult(content=[TextContent(type='text', text='Angle set to 0', annotations=None, meta=None)], structured_content=None, meta=None, data=None, is_error=False) 

🚩result━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩

~/my-mcp👉 uv run /home/nob/文件/lesson/ai_程式設計班/a6/use_mcp_tool.py -a 'http://10.42.0.110:80/mcp' -t "set_servo_angle" -p '{"angle": 180}'
🚩result━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩

CallToolResult(content=[TextContent(type='text', text='Angle set to 180', annotations=None, meta=None)], structured_content=None, meta=None, data=None, is_error=False) 

🚩result━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩

🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞 

~/my-mcp👉 uv run /home/nob/文件/lesson/ai_程式設計班/a5/client_http_mcp.1.py -a 'http://10.42.0.110:80/mcp'
🚩tools━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩

name='set_servo' title=None description='Set SG90 servo angle (0-180)' inputSchema={'properties': {'angle': {'minimum': 0, 'maximum': 180, 'type': 'integer'}}, 'required': ['angle'], 'type': 'object'} outputSchema=None icons=None annotations=None meta=None execution=None 

🚩tools━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩

~/my-mcp👉 uv run /home/nob/文件/lesson/ai_程式設計班/a6/use_mcp_tool.py -a 'http://10.42.0.110:80/mcp' -t "set_servo" -p '{"angle": 0}'
🚩result━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩

CallToolResult(content=[TextContent(type='text', text='{"angle": 0}', annotations=None, meta=None)], structured_content=None, meta=None, data=None, is_error=False) 

🚩result━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩

~/my-mcp👉 uv run /home/nob/文件/lesson/ai_程式設計班/a6/use_mcp_tool.py -a 'http://10.42.0.110:80/mcp' -t "set_servo" -p '{"angle": 180}'
🚩result━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩

CallToolResult(content=[TextContent(type='text', text='{"angle": 180}', annotations=None, meta=None)], structured_content=None, meta=None, data=None, is_error=False) 

🚩result━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩

🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞🎞 

~/v2/tmp👉 /home/nob/文件/lesson/ai_程式設計班/a5/req_remote_mcp.0.sh  'http://10.42.0.110:80/mcp'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   392  100   334  100    58   1425    247 --:--:-- --:--:-- --:--:--  1675
🚩━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩
{"result": {"tools": [{"name": "set_servo_angle", "description": "控制接在 GPIO4 的 SG90 伺服馬達轉動指定角度", "inputSchema": {"properties": {"angle": {"minimum": 0, "type": "integer", "maximum": 180, "description": "0 到 180 的整數角度"}}, "required": ["angle"], "type": "object"}}]}, "id": 1, "jsonrpc": "2.0"}
🚩━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚩