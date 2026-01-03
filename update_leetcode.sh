#!/bin/bash

# 簡單的 LeetCode 更新腳本
# 用法: ./update_leetcode.sh "提交訊息"

set -e  # 如果有錯誤就停止

echo "=== LeetCode 更新腳本 ==="

# 清理 Python 暫存檔
echo "1. 清理暫存檔..."
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -type f -delete 2>/dev/null || true

# 檢查 Git 狀態
echo "2. 檢查 Git 狀態..."
git status --short

# 加入所有變更（排除暫存檔）
echo "3. 加入檔案..."
git add .

# 如果有提供提交訊息就用，否則用預設
if [ -z "$1" ]; then
    commit_msg="update: $(date '+%Y-%m-%d %H:%M:%S')"
else
    commit_msg="$1"
fi

# 提交
echo "4. 提交變更: $commit_msg"
git commit -m "$commit_msg"

# 推送到 GitHub
echo "5. 推送到 GitHub..."
git push origin main

echo "✅ 更新完成！"
