# MCP Agent 跌倒偵測系統

> 基於 Model Context Protocol (MCP) 架構的 AI Agent 視覺監控系統，結合攝影機、伺服馬達與 LLM 實現跌倒偵測與即時追蹤。

## 📌 專案簡介

本專案實作了一個完整的 MCP Agent 系統，展示如何透過 MCP 協議整合：

- **攝影機 MCP Server**：提供影像擷取功能
- **伺服馬達 MCP Server**：控制 PTZ (Pan-Tilt-Zoom) 鏡頭轉動
- **訊息監控 MCP Server**：即時顯示 Agent 決策日誌
- **AI Agent**：使用 Qwen3-VL-2B 視覺語言模型進行影像分析與決策

## 🏗️ 系統架構

\`\`\`
┌─────────────────────────────────────────────────────────────┐
│                        AI Agent                              │
│                    (agent_cam.g5.py)                         │
│                    Port: 8828 (監控畫面)                      │
└───────────────┬─────────────────┬───────────────────────────┘
                │                 │
    ┌───────────▼───────┐ ┌───────▼───────────┐
    │  Camera MCP       │ │  PTZ MCP          │
    │  (SSE / HTTP)     │ │  (HTTP)           │
    │  Port: 8808       │ │  Port: 80         │
    │  mcp_cam.g1.py    │ │  sg90_mcp_a.6.py  │
    └───────────┬───────┘ └───────┬───────────┘
                │                 │
        ┌───────▼───────┐ ┌───────▼───────────┐
        │   USB Cam     │ │   ESP32 + SG90    │
        │   /dev/video0 │ │   伺服馬達         │
        └───────────────┘ └───────────────────┘
\`\`\`

## 🚀 快速開始

### 1. 環境建置

\`\`\`bash
# 建立 uv 虛擬環境
cd ~
uv init v6
cd v6
uv add fastmcp openai opencv-python paho-mqtt aiohttp
\`\`\`

### 2. 啟動 LLM 伺服器 (llama.cpp)

\`\`\`bash
./utils/llama-server.Qwen3-VL-2B.sh
\`\`\`

### 3. 啟動 MCP 伺服器

\`\`\`bash
# 攝影機 MCP (SSE)
uv run mcp_servers/camera/mcp_cam.g1.py

# 訊息監控 MCP (stdio)
uv run mcp_servers/monitor/mcp_msg.g1.py

# ESP32 伺服馬達 MCP (上傳至 ESP32 後自動啟動)
\`\`\`

### 4. 啟動 AI Agent

\`\`\`bash
uv run agents/vision_tracking/agent_cam.g5.py
\`\`\`

### 5. 開啟監控網頁

- Agent 視覺畫面：http://localhost:8828
- 即時日誌：http://localhost:8817
- 攝影機原始串流：http://localhost:8818/mymcp_cam.mjpg

## 📁 目錄結構

\`\`\`
fall-detection-mcp-agent/
├── README.md                    # 專案說明
├── docs/                        # 文件目錄
│   ├── 課程筆記_MCP_Agent.md
│   ├── 架構說明.md
│   └── 部署步驟.md
├── mcp_servers/                 # MCP 伺服器
│   ├── camera/                  # 攝影機 MCP
│   ├── monitor/                 # 日誌監控 MCP
│   ├── servo/                   # 伺服馬達 MCP
│   └── mqtt/                    # MQTT 建置腳本
├── agents/                      # AI Agent
│   ├── vision_tracking/         # 視覺追蹤 Agent
│   └── task_agent/              # 任務型 Agent
├── clients/                     # MCP 客戶端工具
├── utils/                       # 輔助工具
├── env/                         # 環境建置記錄
├── notes/                       # 測試筆記
└── git_notes/                   # Git 操作記錄
\`\`\`

## 🔧 使用技術

- **MCP 協議**：stdio / SSE / Streamable HTTP
- **AI 模型**：Qwen3-VL-2B-Instruct (GGUF)
- **LLM 引擎**：llama.cpp
- **硬體控制**：MicroPython / ESP32
- **通訊**：MQTT / HTTP / WebSocket
- **Python 框架**：FastMCP, FastAPI, OpenCV

## 📖 相關文件

- [課程筆記](docs/課程筆記_MCP_Agent.md)
- [系統架構說明](docs/架構說明.md)
- [完整部署步驟](docs/部署步驟.md)

## 📝 版本記錄

- **v1.0** - 2026/04/01 - 完成基礎 MCP Agent 跌倒偵測系統

