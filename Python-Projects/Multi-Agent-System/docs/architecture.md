# Multi-Agent System 架構說明

## 系統元件

### 1. LLM 設定
使用 OpenAILike 連接到本地 LLM 服務：
- API 位址：http://localhost:8880/v1
- 支援 function calling（可選）

### 2. 智能體定義

#### Agent 1: secret_fact_agent
- 擁有工具：`get_the_secret_fact`
- 功能：回傳秘密事實

#### Agent 2: dumb_fact_agent
- 無工具
- 功能：隨機事實回答

### 3. 通訊架構

| 元件 | 端口 | 功能 |
|------|------|------|
| Message Queue | 8000 | 智能體間訊息傳遞 |
| Control Plane | 8001 | 智能體調度與管理 |
| Agent Server 1 | 8002 | 秘密事實智能體 |
| Agent Server 2 | 8003 | 隨機事實智能體 |

## 使用流程

1. 使用者提出問題
2. Control Plane 接收問題
3. Orchestrator 決定由哪個智能體處理
4. 智能體透過 Message Queue 接收任務
5. 智能體執行任務（可能使用工具）
6. 結果回傳給使用者

## 擴展建議

- 增加更多專業智能體
- 加入智能體之間的協作
- 整合 RAG 檢索功能
- 加入記憶管理機制