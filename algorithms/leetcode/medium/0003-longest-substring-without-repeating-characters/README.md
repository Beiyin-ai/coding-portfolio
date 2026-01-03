# 3. Longest Substring Without Repeating Characters

**完成日期：** 2026-01-04
**難度：** Medium
**標籤：** Hash Table, String, Sliding Window
**連結：** [LeetCode 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## 題目描述
Given a string `s`, find the length of the longest substring without duplicate characters.

### 範例
**範例 1：**
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

**範例 2：**
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

**範例 3：**
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

### 限制條件
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

## 解法：滑動窗口 + 集合（我的解法）

### 程式碼
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()    # 記錄當前窗口中的字符
        left = 0        # 窗口左指針
        max_len = 0     # 最長長度
        
        for right in range(len(s)):
            # 如果當前字符已存在，移動左指針直到字符不再重複
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            # 加入當前字符到集合
            seen.add(s[right])
            
            # 更新最大長度
            max_len = max(max_len, right - left + 1)
        
        return max_len
```

### 解題思路
1. **滑動窗口 (Sliding Window)：**
   - 使用兩個指針 `left` 和 `right` 定義當前窗口
   - `right` 指針向右擴展窗口
   - `left` 指針在遇到重複字符時向右移動

2. **集合記錄字符：**
   - 使用 `set()` 記錄當前窗口中的所有字符
   - 快速檢查字符是否重複（O(1) 時間）

3. **算法步驟：**
   - 遍歷字符串，`right` 從 0 到 n-1
   - 如果 `s[right]` 已在集合中，移動 `left` 指針並從集合中移除字符
   - 將 `s[right]` 加入集合
   - 更新最大長度：`right - left + 1`

### 關鍵點
- 滑動窗口技巧：適用於「最長/最短子字串」問題
- 集合的 O(1) 查找：快速判斷字符是否重複
- 雙指針移動：`right` 總是向右，`left` 只在必要時向右

### 複雜度分析
- **時間複雜度：** O(n)
  - 每個字符最多被 `right` 訪問一次，被 `left` 訪問一次
  - 雖然有 while 迴圈，但每個字符只會被加入和移除集合各一次
- **空間複雜度：** O(min(n, m))
  - m 是字符集大小（ASCII 128，Unicode 更大）
  - 最壞情況下需要存儲所有不重複字符

### 測試範例
```python
# 測試 1: "abcabcbb" → 3
# 測試 2: "bbbbb" → 1
# 測試 3: "pwwkew" → 3
# 測試 4: "" → 0
# 測試 5: " " → 1
# 測試 6: "abba" → 2
# 測試 7: "dvdf" → 3
```

## 其他解法

### 解法2：使用字典記錄字符最後出現位置
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # 記錄字符最後出現的位置
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len
```

### 解法3：使用陣列優化（ASCII 字符）
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 假設是 ASCII 字符集
        last_index = [-1] * 128
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            ascii_val = ord(char)
            if last_index[ascii_val] >= left:
                left = last_index[ascii_val] + 1
            last_index[ascii_val] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len
```

## 解題思路比較

| 方法 | 時間複雜度 | 空間複雜度 | 特點 |
|------|-----------|-----------|------|
| 集合 + 滑動窗口 | O(n) | O(min(n, m)) | 直觀易懂 |
| 字典記錄位置 | O(n) | O(min(n, m)) | 更高效，直接跳躍 |
| 陣列優化 | O(n) | O(m) | 最快，但僅限已知字符集 |

## 學習心得
這題讓我學到：

1. **滑動窗口模式**：解決子字串/子陣列問題的強大技巧
2. **集合 vs 字典**：根據需求選擇合適的資料結構
3. **雙指針技巧**：left 和 right 指針的協同工作
4. **邊界條件處理**：空字串、單一字元、全部重複等情況

這是我的第三個 Medium 題目，滑動窗口是一個非常重要的演算法模式！

## 相關題目
- 159. Longest Substring with At Most Two Distinct Characters (Medium)
- 340. Longest Substring with At Most K Distinct Characters (Medium)
- 424. Longest Repeating Character Replacement (Medium)
- 76. Minimum Window Substring (Hard)

## 下一步計畫
1. 練習更多滑動窗口的變形題目
2. 嘗試用字典優化解法
3. 學習其他字符串處理的高級技巧
