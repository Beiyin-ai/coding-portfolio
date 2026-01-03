# 📚 Coding Portfolio 使用說明

## 🚀 快速開始

### 1. 檢查當前狀態
```bash
cd scripts
./check_problems.sh
```

### 2. 提交新的 LeetCode 題目
```bash
cd scripts
./commit_problem.sh 題號 "題目說明"
# 範例：提交第3題
./commit_problem.sh 3 "Longest Substring Without Repeating Characters"
```

### 3. 更新整個專案
```bash
cd scripts
./update_leetcode.sh "提交訊息"
```

### 4. 清理 Python 暫存檔
```bash
find . -name "__pycache__" -type d -exec rm -rf {} +
find . -name "*.pyc" -type f -delete
```

## 📁 目錄結構

```
coding-portfolio/
├── README.md          # 主說明文件
├── USAGE.md          # 使用說明（本文件）
├── .gitignore        # Git 忽略設定
├── scripts/          # 工具腳本
│   ├── check_problems.sh     # 檢查解題統計
│   ├── commit_problem.sh     # 提交特定題目
│   └── update_leetcode.sh    # 更新整個專案
├── algorithms/       # LeetCode 解題專區
│   ├── leetcode/
│   │   ├── easy/    # Easy 難度題目
│   │   └── medium/  # Medium 難度題目
├── certificates/     # 證書專區
├── learning/         # 學習專區
├── projects/         # 專案專區
└── resources/        # 資源專區
```

## 📊 當前統計
（運行 `./check_problems.sh` 查看最新統計）

## �� 常用指令

```bash
# 進入 scripts 資料夾
cd scripts

# 查看幫助
./commit_problem.sh

# 提交所有變更到 GitHub
git add .
git commit -m "更新說明"
git push origin main
```

## 🆘 問題排除

1. **腳本權限問題**：
   ```bash
   chmod +x scripts/*.sh
   ```

2. **路徑問題**：確保在正確的目錄執行腳本

3. **Git 問題**：檢查是否有未提交的變更
   ```bash
   git status
   ```
