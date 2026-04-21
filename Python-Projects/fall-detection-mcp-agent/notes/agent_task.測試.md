# cam_task.測試.md

~/v6👉 cd agent.task

~/v6/agent.task👉 uv run cam_task.py -v  '../跑步機_客廳.mp4' -m '那個人跌倒了嗎?'

###  -v 後面可以是 0 或 1 表示 USB攝影機 '/dev/video0' 或 '/dev/video1' 或 mp4 檔案路徑 或  網頁串流：'https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8'
###  -m 後面接訊息是要給  agent 的任務 

# 測試 RTSP 串流
uv run cam_task.py -v "rtsp://807e9439d5ca.entrypoint.cloud.wowza.com:1935/app-rC94792j/068b9c9a_stream2" -m "畫面裡有船嗎？"

# 測試 MJPEG HTTP 串流
uv run cam_task.py -v "http://193.231.160.38/axis-cgi/mjpg/video.cgi" -m "擺鐘有在動嗎？"

# 測試網路 MP4 影片
uv run cam_task.py -v "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4" -m "兔子在做什麼？"

### 開新的 終端機

~/v6/agent.task👉 uv run agent_task.py

# 監視 agent_task.py 收到  MCP伺服器  cam_task.py 傳來的畫面
firefox  --window-size 640,320  --new-window 'http://localhost:8828/monitor' &

# MCP伺服器  mcp_message.py 提供給 agent 傳出的訊息到網頁
firefox  --window-size 640,320  --new-window 'http://localhost:8817' &

# MCP伺服器  cam_task.py  監視畫面
firefox  --window-size 640,320  --new-window 'http://localhost:8818/mymcp_cam.mjpg' &

### 開新的 終端機  給  agent 新的任務 

👉 mosquitto_pub -h 172.17.0.1 -p 1883 -t 'agent/task' -m '有人跌倒了嗎？簡單回答'
👉 mosquitto_pub -h 172.17.0.1 -p 1883 -t 'agent/task' -m '那個人有沒危險？簡單回答'
👉 mosquitto_pub -h 172.17.0.1 -p 1883 -t 'agent/task' -m '跌倒的那個人有沒有躺平？'
👉 mosquitto_pub -h 172.17.0.1 -p 1883 -t 'agent/task' -m '跌倒的那個人有沒有躺下？'
👉 mosquitto_pub -h 172.17.0.1 -p 1883 -t 'agent/task' -m '那個人跌了幾次'
👉 mosquitto_pub -h 172.17.0.1 -p 1883 -t 'agent/task' -m '跌倒的人有沒躺平在跑步機上？'
👉 mosquitto_pub -h 172.17.0.1 -p 1883 -t 'agent/task' -m '跌倒的人有沒躺在跑步機上？'
👉 mosquitto_pub -h 172.17.0.1 -p 1883 -t 'agent/task' -m '跌倒的人躺下時跑步機有沒停止？'

https://gemini.google.com/share/948c06a80f0a
https://gemini.google.com/share/b25906818a0a