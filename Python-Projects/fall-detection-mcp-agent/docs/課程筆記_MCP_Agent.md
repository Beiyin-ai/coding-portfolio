# MCP 與 Agent 課程筆記

> 上課日期：2026/04/01

## 一、MCP 的三種傳輸方式

| 方式 | 說明 | 適用場景 |
|------|------|---------|
| **stdio** | 標準輸入輸出，本地程序間通訊 | 同台電腦的 MCP |
| **SSE** | Server-Sent Events，伺服器主動推送 | 即時訊息、狀態更新 |
| **Streamable HTTP** | HTTP 串流傳輸，雙向通訊 | 跨網路、大資料 |

## 二、核心觀念

> MCP Server 本質：幫你把「硬體」變成「API」

## 三、系統架構

```
AI Agent (決策中心) → MCP Server (硬體抽象層) → 設備 (CAM / Servo)
```

## 四、通訊埠分配

| 角色 | Port | 協定 |
|------|------|------|
| Camera MCP | 8808 | SSE |
| Camera 串流 | 8818 | HTTP |
| Monitor MCP | 8817 | WebSocket |
| Agent 畫面 | 8828 | HTTP |
| MQTT Broker | 1883 | MQTT |
| PTZ MCP (ESP32) | 80 | HTTP |
| LLM (llama.cpp) | 8880 | HTTP |
