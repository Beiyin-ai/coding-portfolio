#!/bin/bash

echo "開始為所有題目添加完成日期..."

# 函數：添加完成日期
add_completion_date() {
    local file="$1"
    local date="$2"
    
    if [ -f "$file" ]; then
        # 在標題行後添加完成日期
        sed -i "0,/# [0-9]/{
            s/# \([0-9].*\)/# \1\n\n**完成日期：** $date  /
        }" "$file"
        
        echo "✅ $(basename $(dirname "$file")) 日期已添加: $date"
    fi
}

# Two Sum
add_completion_date "algorithms/leetcode/easy/0001-two-sum/README.md" "2025-12-22"

# Palindrome Number
add_completion_date "algorithms/leetcode/easy/0009-palindrome-number/README.md" "2025-12-23"

# Valid Parentheses
add_completion_date "algorithms/leetcode/easy/0020-valid-parentheses/README.md" "2025-12-31"

# Contains Duplicate
add_completion_date "algorithms/leetcode/easy/0217-contains-duplicate/README.md" "2025-12-28"

# Valid Anagram
add_completion_date "algorithms/leetcode/easy/0242-valid-anagram/README.md" "2025-12-29"

# First Unique Character in a String（有優化更新）
add_completion_date "algorithms/leetcode/easy/0387-first-unique-character-in-a-string/README.md" "2025-12-30（首次完成），2026-01-02（優化更新）"

# Fizz Buzz（有優化更新）
add_completion_date "algorithms/leetcode/easy/0412-fizz-buzz/README.md" "2025-12-27（首次完成），2026-01-02（優化更新）"

# Running Sum of 1d Array
add_completion_date "algorithms/leetcode/easy/1480-running-sum-of-1d-array/README.md" "2025-12-26"

# Richest Customer Wealth（有優化）
add_completion_date "algorithms/leetcode/easy/1672-richest-customer-wealth/README.md" "2025-12-25（首次完成），後續優化"

# Add Two Integers
add_completion_date "algorithms/leetcode/easy/2235-add-two-integers/README.md" "2025-12-24"

# Best Time to Buy and Sell Stock
add_completion_date "algorithms/leetcode/easy/0121-best-time-to-buy-and-sell-stock/README.md" "2026-01-03"

# Group Anagrams (Medium)
add_completion_date "algorithms/leetcode/medium/0049-group-anagrams/README.md" "2026-01-01"

# Top K Frequent Elements (Medium)
add_completion_date "algorithms/leetcode/medium/0347-top-k-frequent-elements/README.md" "2026-01-02"

echo ""
echo "所有完成日期已添加完成！"
