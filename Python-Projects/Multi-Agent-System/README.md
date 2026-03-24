# Multi-Agent System

基於 LlamaIndex 的多智能體協作系統。

## ✨ 功能特色

- 🤖 **多智能體協作**：多個專業智能體協同工作
- 📡 **訊息佇列通訊**：智能體之間透過訊息佇列溝通
- 🎯 **控制平面調度**：智能體調度器負責任務分配
- 🔌 **本地 LLM 整合**：連接到本地 LLM 服務 (localhost:8880)

## 🏗️ 系統架構

```
┌─────────────────────────────────────────┐
│           Control Plane (8001)          │
│         Agent Orchestrator              │
└─────────────────────────────────────────┘
                    │
┌─────────────────────────────────────────┐
│         Message Queue (8000)            │
└─────────────────────────────────────────┘
         │                       │
┌─────────────────┐   ┌─────────────────┐
│ Agent Server 1  │   │ Agent Server 2  │
│   (8002)        │   │   (8003)        │
│ secret_fact     │   │ dumb_fact       │
└─────────────────┘   └─────────────────┘
```

## 📦 安裝需求

- Python 3.8+
- llama-agents
- llama-index
- openai

## 🚀 快速開始

1. 安裝依賴套件：
   ```bash
   pip install -r requirements.txt
   ```

2. 確保本地 LLM 服務已啟動：
   ```bash
   # 確認 localhost:8880 服務正常
   curl http://localhost:8880/v1/models
   ```

3. 執行程式：
   ```bash
   python agent_server.py
   ```

## 📁 專案結構

```
Multi-Agent-System/
├── README.md          # 專案說明
├── requirements.txt   # 依賴套件
├── .gitignore        # Git 忽略規則
├── agent_server.py   # 多智能體伺服器
└── docs/
    └── architecture.md # 架構說明
```

## 🔧 設定說明

本專案需要連接到本地 LLM 服務（預設位址：http://localhost:8880/v1）
請確保在執行程式前已啟動 LLM 服務。

## 📝 授權條款

MIT License
