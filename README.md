# 👋 邱佩吟 | Chiu Pei-Yin
### 轉職 | 雲端 × IoT × 全端 | 快速學習 × 實戰導向

> 從外語與國際貿易背景成功轉型，證明我擁有強大的學習引擎。**兩個月內從零考取 ITS Python 國際證照**，現正系統化建構雲端、IoT 與全端技能。具備 AWS EC2 實戰部署經驗、完整 IoT 系統整合能力，近期聚焦於 **ESG 節能監控** 與 **資料中心能耗可視化** 領域，期待加入重視成長與協作的技術團隊。
> 
> ![AWS](https://img.shields.io/badge/AWS-EC2-orange?logo=amazonaws) ![Python](https://img.shields.io/badge/Python-ITS-blue?logo=python) ![Linux](https://img.shields.io/badge/Linux-Ubuntu-black?logo=linux) ![IoT](https://img.shields.io/badge/IoT-ESP32-green?logo=espressif) ![Node-RED](https://img.shields.io/badge/Node--RED-正在學習-red?logo=nodered)
> 
> Successfully transitioned from linguistics and international trade into tech, demonstrating strong learning ability. **Earned ITS Python International Certification from scratch in 2 months.** Currently building cloud, IoT and full-stack skills. Hands-on experience with AWS EC2 deployment, IoT system integration, and **energy monitoring for ESG applications**. Eager to join a growth-oriented tech team.

---

## 🏗️ 精選專案 | Featured Projects

### ❶ ESP32 智慧能源監控系統（ESG × 節能監控）
**使用技術：** ESP32 · Arduino · Python Flask · MySQL · INA219 · DHT22 · OLED · LED

**專案亮點：**
- **完整能耗監測鏈路**：整合電量（INA219）、溫濕度（DHT22）、光照（LDR）、太陽能電壓等感測器，實現即時數據採集與上傳
- **智慧視覺化反饋**：LED 燈條根據即時用電量與太陽能貢獻自動變色（彩虹/綠/藍/紅），直觀呈現能耗狀態
- **可擴展至資料中心層級**：此架構可應用於機櫃用電監測、PUE 優化、空調能耗分析，為 **ESG 節能減碳** 提供數據基礎
- **模組化設計**：分層管理硬體控制、數據上傳、後端 API，易於維護與擴充

**🔗 [查看完整專案](https://github.com/Beiyin-ai/coding-portfolio/tree/main/projects/ESP32-Energy-Monitor)**

---

### ❷ 端到端 IoT 溫濕度監測系統（MQTT × 資料中樞）
**使用技術：** Linux (Ubuntu) · Mosquitto MQTT · Python · Docker · ESP32

**專案亮點：**
- **本地伺服器維運**：部署並配置 Mosquitto MQTT Broker，建立穩定的物聯網數據中樞
- **硬軟體整合**：整合 ESP32 感測器與 Python 後台服務，實現完整數據鏈路
- **後台服務開發**：開發 Python 服務訂閱 MQTT 主題、解析數據、執行異常判斷
- **適用於資料中心監控**：MQTT 為資料中心常見的感測器數據匯流協定，此專案展示完整實作能力

**🔗 [查看專案](https://github.com/Beiyin-ai/coding-portfolio/tree/main/Python-Projects/IoT-MQTT-System)**

---

### ❸ AWS EC2 完整部署實戰：LAMP + MQTT 服務架設
**使用技術：** AWS EC2 · Ubuntu · Apache · MySQL · PHP · Mosquitto MQTT · Linux · Bash

**專案亮點：**
- **完整雲端部署流程**：從帳號註冊、執行個體啟動、安全群組設定到服務安裝
- **自動化部署腳本**：撰寫 Bash 腳本一鍵安裝 LAMP 環境與 MQTT Broker
- **維運與安全實務**：設定固定 IP、配置防火牆、管理使用者權限
- **詳細技術文檔**：362 行逐步教學，展示系統化思維與知識分享能力

**🔗 [查看完整部署指南](https://github.com/Beiyin-ai/coding-portfolio/tree/main/Cloud-Deployment-Guides/AWS-LAMP-MQTT-Setup)**

---

### ❹ 台灣水庫即時監測與分析系統
**使用技術：** Python · Selenium · BeautifulSoup4 · pandas · matplotlib

**專案亮點：**
- **自動化數據採集**：開發爬蟲抓取 21 座水庫即時數據
- **高效數據處理**：40 秒內完成爬取、解析、視覺化全流程
- **產出完整報表**：輸出 CSV 資料檔與視覺化長條圖，建立監測分析流程
- **監控系統開發基礎**：此專案展示數據採集、處理、視覺化的完整能力，可延伸至各類監控應用

**🔗 [查看專案](https://github.com/Beiyin-ai/coding-portfolio/tree/main/Python-Projects/Taiwan-Reservoir-Monitoring-System)**

---

### ❺ 多模型 MNIST 手寫數字辨識 API（FastAPI × 模型部署）
**使用技術：** FastAPI · Docker · PyTorch · 7 種模型架構 · HTML/CSS

**專案亮點：**
- **REST API 服務**：提供多模型即時推論 API，支援 CNN、ViT 等不同架構
- **容器化部署**：撰寫 Dockerfile 與 docker-compose，一鍵啟動完整服務
- **前端展示頁面**：提供簡易 Web 介面，展示 API 呼叫與結果呈現
- **AI 應用落地能力**：展現將模型封裝為可服務 API 的實務經驗

**🔗 [查看專案](https://github.com/Beiyin-ai/coding-portfolio/tree/main/Python-Projects/MNIST-MultiModel-FastAPI-API)**

---

## 🛠️ 技術能力 | Technical Skills

**☁️ 雲端平台**
- AWS EC2 實戰部署（LAMP / MQTT）· 安全群組設定 · 彈性 IP 管理
- 具 Docker 容器化經驗，熟悉 docker-compose 多服務配置

**🖥️ 系統與維運**
- Linux (Ubuntu) 服務管理 · Bash 自動化腳本
- Git 版本控制 · 基礎 CI/CD 概念

**💻 程式開發**
- **Python**：ITS 國際認證｜爬蟲、數據分析、FastAPI 後端開發
- **IoT**：ESP32（Arduino / MicroPython）｜MQTT 協定實作｜感測器整合（電量、溫濕度、光照）
- **資料庫**：MySQL 設計與 SQL 查詢優化
- **嵌入式**：ESP32 韌體開發、感測器數據採集、LED 燈號控制

**📊 資料視覺化與監控（學習中）**
- **Node-RED**：物聯網流程編程，用於快速建立監控儀表板
- 目標：將能耗監控數據視覺化，模擬資料中心 PUE 監控面板

---

## 📜 證照與語言 | Certifications & Languages

**專業證照**
- ITS Python 國際證照（已取得，證照 PDF 附於 GitHub）
- TOEIC 795（聽/讀）· DELE B1 西班牙語能力證書
- 國貿技術士丙級證照

**語言能力**
- 中文（母語）· 英文（精通，TOEIC 795）· 西班牙文（中等，DELE B1）

---

## 🎯 近期目標與學習方向 | Current Focus

- **Node-RED 儀表板開發**：將 ESP32-Energy-Monitor 的能耗數據透過 Node-RED 視覺化，建立即時監控介面
- **資料中心能耗監控知識**：學習 PUE 計算方式、SNMP / Modbus 協定基礎，強化 ESG 節能領域專業
- **TLS/SSL 憑證實務**：為 MQTT 服務加入加密通訊，提升系統安全性
- **準備 AWS Solutions Architect 認證**：深化雲端架構設計能力

---

## 🎯 核心優勢 | Core Strengths

1. **🚀 快速學習與執行力**：兩個月從零考取專業認證，並自主完成多個實戰專案
2. **🧠 紮實的邏輯與問題解決能力**：透過實戰專案鍛鍊系統化思維與除錯能力
3. **☁️ 雲端實戰經驗**：具備 AWS EC2 完整部署經驗，從概念到上線的完整流程實踐
4. **🔌 IoT 系統整合能力**：從感測器、韌體、MQTT 到後端服務的完整數據鏈路實作
5. **🌱 ESG 節能應用**：能源監控專案可擴展至資料中心層級，展現對節能減碳議題的關注與實踐
6. **📚 文檔化與知識分享**：重視技術文件撰寫，建立清晰的部署指南與專案說明

---

## 📬 聯絡方式 | Contact Information

- **📧 Email：** pei.yin.s.chiu@gmail.com
- **📞 Phone：** 0983-689-716
- **🐙 GitHub：** [github.com/Beiyin-ai](https://github.com/Beiyin-ai)
- **📍 地點：** 台北市、新北市 · 可配合上班地點
- **💼 求職狀態：** 積極尋找雲端工程師、IoT 工程師、後端工程師、系統整合工程師相關職位

---

> *「從感測器到雲端，我正走在成為可靠 IoT 與雲端工程師的路上。」*
> *"From sensors to the cloud, I am on the path to becoming a reliable IoT and cloud engineer."*
