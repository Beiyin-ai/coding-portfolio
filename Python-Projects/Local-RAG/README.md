# Local RAG System

一個完全在本機運作的檢索增強生成（RAG）系統基礎環境。

## ✨ 功能特色

- 🔒 **100% 本地運作**：所有資料和模型都在本地，確保資料安全
- 🌏 **多語言支援**：支援中英文混合查詢
- 📦 **環境檢查**：自動檢查必要的環境變數
- 🚀 **快速啟動**：一行指令完成環境設定

## 📁 專案結構

```
Local-RAG/
├── README.md          # 專案說明
├── requirements.txt   # 依賴套件
├── .gitignore        # Git 忽略規則
├── get_env_var.py    # 環境變數檢查工具
└── a4_rag_環境.txt   # 環境建置步驟
```

## 🚀 安裝方式

```bash
# 安裝依賴套件
pip install -r requirements.txt

# 設定模型快取目錄
export SENTENCE_TRANSFORMERS_HOME="$HOME/model/"

# 檢查環境變數是否設定成功
python get_env_var.py
```

## 📦 安裝套件

```bash
# 使用 uv 安裝（推薦）
uv add sentence-transformers chromadb faiss-cpu openai

# 或使用 pip 安裝
pip install sentence-transformers chromadb faiss-cpu openai
```

## 🔧 環境設定

### 設定模型快取路徑

將以下內容加入 `~/.bashrc` 或 `~/.zshrc`：

```bash
export SENTENCE_TRANSFORMERS_HOME="$HOME/model/"
```

### 檢查環境變數

```bash
python get_env_var.py
# 輸出：SENTENCE_TRANSFORMERS_HOME=/home/user/model/
```

## 📝 快速開始

1. 安裝依賴套件
2. 設定環境變數
3. 確認 LLM 服務已啟動（預設位址：http://localhost:8880/v1）
4. 執行其他 RAG 專案（FAISS-RAG、ChromaDB-RAG）

## 📝 授權條款

MIT License
