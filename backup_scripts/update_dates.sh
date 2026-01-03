#!/bin/bash

echo "開始更新各題目完成日期..."

# Two Sum
cd algorithms/leetcode/easy/0001-two-sum 2>/dev/null && sed -i 's/完成日期：.*/完成日期：2025-12-22/' README.md 2>/dev/null && echo "✓ 0001 更新完成" || echo "⚠ 0001 跳過"

# Palindrome Number
cd ../../../../ && cd algorithms/leetcode/easy/0009-palindrome-number 2>/dev/null && sed -i 's/完成日期：.*/完成日期：2025-12-23/' README.md 2>/dev/null && echo "✓ 0009 更新完成" || echo "⚠ 0009 跳過"

# Valid Parentheses
cd ../../../../ && cd algorithms/leetcode/easy/0020-valid-parentheses 2>/dev/null && sed -i 's/完成日期：.*/完成日期：2025-12-31/' README.md 2>/dev/null && echo "✓ 0020 更新完成" || echo "⚠ 0020 跳過"

# Contains Duplicate
cd ../../../../ && cd algorithms/leetcode/easy/0217-contains-duplicate 2>/dev/null && sed -i 's/完成日期：.*/完成日期：2025-12-28/' README.md 2>/dev/null && echo "✓ 0217 更新完成" || echo "⚠ 0217 跳過"

# Valid Anagram
cd ../../../../ && cd algorithms/leetcode/easy/0242-valid-anagram 2>/dev/null && sed -i 's/完成日期：.*/完成日期：2025-12-29/' README.md 2>/dev/null && echo "✓ 0242 更新完成" || echo "⚠ 0242 跳過"

# First Unique Character
cd ../../../../ && cd algorithms/leetcode/easy/0387-first-unique-character-in-a-string 2>/dev/null && sed -i 's/完成日期：.*/完成日期：2025-12-30（首次完成），2026-01-02（優化更新）/' README.md 2>/dev/null && echo "✓ 0387 更新完成" || echo "⚠ 0387 跳過"

# Fizz Buzz
cd ../../../../ && cd algorithms/leetcode/easy/0412-fizz-buzz 2>/dev/null && sed -i 's/完成日期：.*/完成日期：2025-12-27（首次完成），2026-01-02（優化更新）/' README.md 2>/dev/null && echo "✓ 0412 更新完成" || echo "⚠ 0412 跳過"

# Running Sum
cd ../../../../ && cd algorithms/leetcode/easy/1480-running-sum-of-1d-array 2>/dev/null && sed -i 's/完成日期：.*/完成日期：2025-12-26/' README.md 2>/dev/null && echo "✓ 1480 更新完成" || echo "⚠ 1480 跳過"

# Richest Customer Wealth
cd ../../../../ && cd algorithms/leetcode/easy/1672-richest-customer-wealth 2>/dev/null && sed -i 's/完成日期：.*/完成日期：2025-12-25（首次完成），後續優化/' README.md 2>/dev/null && echo "✓ 1672 更新完成" || echo "⚠ 1672 跳過"

# Add Two Integers
cd ../../../../ && cd algorithms/leetcode/easy/2235-add-two-integers 2>/dev/null && sed -i 's/完成日期：.*/完成日期：2025-12-24/' README.md 2>/dev/null && echo "✓ 2235 更新完成" || echo "⚠ 2235 跳過"

# Best Time to Buy and Sell Stock
cd ../../../../ && cd algorithms/leetcode/easy/0121-best-time-to-buy-and-sell-stock 2>/dev/null && sed -i 's/完成日期：.*/完成日期：2026-01-03/' README.md 2>/dev/null && echo "✓ 0121 更新完成" || echo "⚠ 0121 跳過"

# Group Anagrams (Medium)
cd ../../../../ && cd algorithms/leetcode/medium/0049-group-anagrams 2>/dev/null && sed -i 's/完成日期：.*/完成日期：2026-01-01/' README.md 2>/dev/null && echo "✓ 0049 更新完成" || echo "⚠ 0049 跳過"

# Top K Frequent Elements (Medium)
cd ../../../../ && cd algorithms/leetcode/medium/0347-top-k-frequent-elements 2>/dev/null && sed -i 's/完成日期：.*/完成日期：2026-01-02/' README.md 2>/dev/null && echo "✓ 0347 更新完成" || echo "⚠ 0347 跳過"

echo ""
echo "所有日期更新完成！"
