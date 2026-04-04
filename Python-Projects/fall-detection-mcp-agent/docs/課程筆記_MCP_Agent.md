# MCP 與 Agent 課程筆記

> 上課日期：2026/04/01
> 主題：Model Context Protocol (MCP) 與 AI Agent 架構實作

## 一、MCP 的三種傳輸方式

### 1. SSE (Server-Sent Events)
- 一種讓伺服器主動推送資料給客戶端的技術
- 常用在 MCP 的即時通訊
- 適合：即時訊息、狀態更新、AI token 輸出

### 2. Streamable HTTP MCP
- 透過 HTTP 使用串流方式傳輸的 MCP 實作
- 讓 AI 與工具之間可以雙向持續傳遞訊息
- 適合：長時間任務、大資料傳輸

### 3. stdio (標準輸入輸出)
- MCP 客戶端（如 AI agent）透過標準輸入流傳送請求給 MCP server
- 從標準輸出流讀取回應
- 適合本地程序間通訊，無需透過 HTTP 或網路

### 4. 跨電腦通訊
- SSE 與 Streamable HTTP MCP 可跨電腦：基於 HTTP，可以讓 MCP server 和 client（agent）分別執行在不同電腦上
- MCP Studio 搭配外掛：在同一台電腦使用時，需要透過外掛方式連接（本地 stdio 或 local HTTP）

## 二、HTTP vs SSE 核心差異

| 項目 | HTTP | SSE |
|------|------|-----|
| 連線方式 | 一次請求一次回覆 | 一次連線持續推送 |
| 資料方向 | Client → Server | Server → Client |
| 是否需要一直重新請求 | 要 | 不用 |
| 適合場景 | 取圖片、下載檔案、送指令 | 即時訊息、快照更新、AI token 輸出 |

## 三、系統架構圖解

### 核心角色

| 角色 | 檔案 | 功能 | Port |
|------|------|------|------|
| AI Agent | agent_task.py / agent_cam.g5.py | 決策中心，接收指令、呼叫工具 | 8828 |
| Camera MCP | cam_task.py / mcp_cam.g1.py | 攝影機控制、影像擷取 | 8808 (MCP) / 8818 (串流) |
| Monitor MCP | mcp_msg.g1.py / mcp_message.py | 即時日誌顯示 | 8817 |
| PTZ MCP | sg90_mcp_a.6.py | 伺服馬達控制 | 80 |
| MQTT Broker | mosquitto | 訊息派發中心 | 1883 |

### 通訊分流設計

- **影像串流**：HTTP (Port 8818) - 一次性大量傳輸
- **即時訊息**：SSE (Port 8817) - 伺服器持續推送
- **任務派發**：MQTT (Port 1883) - 發布/訂閱模式
- **工具呼叫**：HTTP / SSE (Port 8808, 80) - MCP 協議

## 四、MCP Server 的本質

> 幫你把「硬體」變成「API」

- ESP32 / CAM → MCP Server → AI / Agent 可呼叫
- 使用 FastAPI 實作 MCP server 的優勢：
  - 非同步 (async) 適合 AI/IoT
  - 支援 SSE / Streaming
  - 效能比 Flask 好

## 五、系統運作流程

### 流程1：AI 控制攝影機

1. AI 發出指令
2. AI Agent 接收
3. 透過 MQTT 發布命令
4. CAM 訂閱 → 收到命令
5. CAM 執行（拍照/串流）

### 流程2：影像回傳分析

1. CAM 存影像 (jpg)
2. MQTT Broker 收到
3. AI Agent / 終端機訂閱
4. 收到畫面 → 做分析或顯示

### 流程3：終端機控制

1. 終端機下指令
2. MQTT 送給 AI Agent 或 CAM
3. 執行操作

## 六、關鍵概念總結

- **MQTT**：訊息派發中心（不用直接連設備）
- **AI Agent**：決策中心
- **MCP**：模組化服務
- **Publish / Subscribe**：核心模式

> 一句話總結：AI 不直接控制設備，而是透過 Agent + MCP 去「發布/訂閱」訊息來控制整個系統。

## 七、跌倒偵測應用

本系統實際應用於跌倒偵測場景：

1. **感知層**：Camera MCP 持續擷取影像
2. **決策層**：AI Agent 使用 Qwen3-VL-2B 分析畫面
   - 判斷是否有「人」
   - 判斷是否「跌倒/躺平」
   - 判斷目標物位置（左/中/右）
3. **執行層**：
   - 發現目標偏離中心 → PTZ MCP 轉動伺服馬達追蹤
   - 偵測到跌倒 → 透過 Monitor MCP 發出警報
   - 可透過 MQTT 發送通知到其他系統

