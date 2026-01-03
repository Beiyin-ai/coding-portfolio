#!/bin/bash

echo "=== LeetCode 解題統計 ==="
echo ""

# 統計題目數量
EASY_COUNT=$(find ../algorithms/leetcode/easy -maxdepth 1 -type d 2>/dev/null | wc -l)
MEDIUM_COUNT=$(find ../algorithms/leetcode/medium -maxdepth 1 -type d 2>/dev/null | wc -l)
HARD_COUNT=$(find ../algorithms/leetcode/hard -maxdepth 1 -type d 2>/dev/null | wc -l)

# 減去 1 因為每個目錄都包含父目錄本身
EASY_COUNT=$((EASY_COUNT > 0 ? EASY_COUNT - 1 : 0))
MEDIUM_COUNT=$((MEDIUM_COUNT > 0 ? MEDIUM_COUNT - 1 : 0))
HARD_COUNT=$((HARD_COUNT > 0 ? HARD_COUNT - 1 : 0))
TOTAL=$((EASY_COUNT + MEDIUM_COUNT + HARD_COUNT))

echo "📊 統計結果："
echo "  Easy:   $EASY_COUNT 題"
echo "  Medium: $MEDIUM_COUNT 題"
echo "  Hard:   $HARD_COUNT 題"
echo "  --------------------"
echo "  總計:   $TOTAL 題"

echo ""
echo "📁 最近新增的題目："
ls -1td ../algorithms/leetcode/*/*/ 2>/dev/null | head -5 | while read dir; do
    dirname=$(basename "$dir")
    problem_num=$(echo "$dirname" | cut -d'-' -f1)
    problem_name=$(echo "$dirname" | cut -d'-' -f2- | tr '-' ' ')
    difficulty=$(basename $(dirname "$dir"))
    echo "  #$problem_num - $problem_name ($difficulty)"
done

echo ""
echo "🔄 Git 狀態："
git status --short 2>/dev/null || echo "  不在 Git 倉庫中"
