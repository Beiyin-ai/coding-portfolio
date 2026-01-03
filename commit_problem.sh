#!/bin/bash

# 提交特定 LeetCode 題目的腳本
# 用法: ./commit_problem.sh "題號" "簡短說明"

if [ -z "$1" ]; then
    echo "請提供題號，例如: ./commit_problem.sh 3"
    exit 1
fi

PROBLEM_NUM="$1"
DESCRIPTION="${2:-新增題目 $PROBLEM_NUM 解法}"

echo "=== 提交 LeetCode 題目 #$PROBLEM_NUM ==="

# 尋找題目資料夾
PROBLEM_DIR=""
if [ -d "algorithms/leetcode/easy/$(printf '%04d' $PROBLEM_NUM)-"* ] 2>/dev/null; then
    PROBLEM_DIR=$(find algorithms/leetcode/easy -name "$(printf '%04d' $PROBLEM_NUM)-*" -type d 2>/dev/null | head -1)
elif [ -d "algorithms/leetcode/medium/$(printf '%04d' $PROBLEM_NUM)-"* ] 2>/dev/null; then
    PROBLEM_DIR=$(find algorithms/leetcode/medium -name "$(printf '%04d' $PROBLEM_NUM)-*" -type d 2>/dev/null | head -1)
fi

if [ -z "$PROBLEM_DIR" ]; then
    echo "❌ 找不到題目 #$PROBLEM_NUM 的資料夾"
    exit 1
fi

echo "找到資料夾: $PROBLEM_DIR"

# 清理暫存檔
find "$PROBLEM_DIR" -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
find "$PROBLEM_DIR" -name "*.pyc" -type f -delete 2>/dev/null || true

# 加入檔案
git add "$PROBLEM_DIR"
git add algorithms/README.md

# 提交
git commit -m "feat: add solution for #$PROBLEM_NUM - $DESCRIPTION"

# 推送到 GitHub
git push origin main

echo "✅ 題目 #$PROBLEM_NUM 提交完成！"
