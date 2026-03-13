# Local RAG System

一個完全在本機運作的檢索增強生成（RAG）系統，不需要將資料上傳到雲端。

## ✨ 功能特色

- 🔒 **100% 本地運作**：所有資料和模型都在本地，確保資料安全
- 🌏 **多語言支援**：支援中英文混合查詢
- 🚀 **快速檢索**：使用 FAISS 向量資料庫進行相似度搜尋
- 💬 **LLM 整合**：可連接本地 LLM 服務（localhost:8880）生成答案

## 📦 安裝需求

- Python 3.8+
- sentence-transformers
- faiss-cpu
- openai
- numpy

## 🚀 快速開始

1. 安裝依賴套件：
   ```bash
   pip install -r requirements.txt
   ```

2. 設定模型快取目錄：
   ```bash
   export SENTENCE_TRANSFORMERS_HOME="$HOME/model/"
   ```

3. 執行程式：
   ```bash
   python basic_rag.py    # 基礎檢索版本
   python complete_rag.py # 完整 RAG 版本
   ```

## 📁 專案結構

```
Local-RAG/
├── README.md          # 專案說明
├── requirements.txt   # 依賴套件
├── .gitignore        # Git 忽略規則
├── basic_rag.py      # 基礎檢索功能
└── complete_rag.py   # 完整 RAG 功能
```

## 🔧 設定說明

本專案需要連接到本地 LLM 服務（預設位址：http://localhost:8880/v1）
請確保在執行程式前已啟動 LLM 服務。

## 📝 授權條款

MIT License
