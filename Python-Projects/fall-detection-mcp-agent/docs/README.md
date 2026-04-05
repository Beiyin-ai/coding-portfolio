# MCP Agent 跌倒偵測系統

> 基於 Model Context Protocol (MCP) 的 AI Agent 視覺監控系統，實現跌倒偵測與即時追蹤。

## 快速開始

```bash
# 環境建置
uv init v6 && cd v6
uv add fastmcp openai opencv-python paho-mqtt aiohttp

# 啟動 Camera MCP
uv run mcp_servers/camera/mcp_cam.g1.py

# 啟動 Monitor MCP
uv run mcp_servers/monitor/mcp_msg.g1.py

# 啟動 Agent
uv run agents/vision_tracking/agent_cam.g5.py
```

## 監控網頁

| 服務 | URL |
|------|-----|
| Agent 視覺畫面 | http://localhost:8828 |
| 即時日誌 | http://localhost:8817 |
| 攝影機串流 | http://localhost:8818/mymcp_cam.mjpg |

## 目錄結構

```
fall-detection-mcp-agent/
├── README.md
├── docs/
├── mcp_servers/
├── agents/
├── clients/
├── utils/
├── env/
├── notes/
└── git_notes/
```

## 技術使用

- MCP 協議：stdio / SSE / HTTP
- AI 模型：Qwen3-VL-2B (GGUF)
- LLM 引擎：llama.cpp
- 硬體：ESP32 + SG90 伺服馬達
