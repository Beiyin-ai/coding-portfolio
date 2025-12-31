# 20. Valid Parentheses

**難度：** Easy  
**標籤：** String, Stack  
**連結：** [LeetCode 20](https://leetcode.com/problems/valid-parentheses/)

## 題目描述
Given a string `s` containing just the characters `'('`, `')'`, `'{\'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### 範例
**範例 1：**
```
Input: s = "()"
Output: true
```

**範例 2：**
```
Input: s = "()[]{}"
Output: true
```

**範例 3：**
```
Input: s = "(]"
Output: false
```

**範例 4：**
```
Input: s = "([])"
Output: true
```

**範例 5：**
```
Input: s = "([)]"
Output: false
```

### 限制條件
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}\'`.

## 解法 1：使用 Stack（我的解法）

### 程式碼
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            elif ch in pairs:
                if not stack:
                    return False
                if stack.pop() != pairs[ch]:
                    return False

        return not stack
```

### 解題思路
1. **使用 Stack 資料結構**：因為括號匹配需要「後進先出」的特性
2. **建立映射關係**：`pairs = {")": "(", "]": "[", "}": "{"}`
3. **遍歷字串**：
   - 遇到**開括號**（`(`, `[`, `{`）：推入 stack
   - 遇到**閉括號**（`)`, `]`, `}`）：
     - 如果 stack 為空 → 返回 False（沒有對應的開括號）
     - 如果 stack 頂部不匹配 → 返回 False
     - 如果匹配 → 彈出 stack 頂部
4. **最終檢查**：如果 stack 為空 → 所有括號都正確匹配

### 關鍵點
- **Stack 的選擇**：Python 中可以用 list 模擬 stack
- **映射方向**：注意映射是 `閉括號 → 開括號`，這樣方便檢查匹配
- **邊界條件**：
  - 空字串：應返回 True（題目說長度 ≥ 1）
  - 只有閉括號：stack 為空時直接返回 False
  - 只有開括號：最後 stack 不為空，返回 False

### 複雜度分析
- **時間複雜度：O(n)** - 只需一次遍歷
- **空間複雜度：O(n)** - 最壞情況下所有字符都是開括號

### 測試範例
```python
測試 1: "()" → True
測試 2: "()[]{}" → True  
測試 3: "(]" → False
測試 4: "([])" → True
測試 5: "([)]" → False
測試 6: "{" → False
測試 7: "}" → False
測試 8: "{([])}" → True
```

### 學習心得
這題讓我學習到：
1. **Stack 的應用場景**：需要後進先出、匹配、對稱等問題
2. **映射表的設計**：從閉括號映射到開括號更直觀
3. **邊界條件處理**：空 stack 的情況需要特別注意
4. **Python 的 in 操作**：`char in mapping.values()` 可以用來判斷是否為開括號

這題是 Stack 的經典應用，在編譯器、表達式求值等場景都有類似應用。

### 相關題目
- [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) (Hard)
- [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) (Medium)
- [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) (Medium)

### 下一步計畫
1. 嘗試用其他語言實現（如 Kotlin）
2. 練習相關的括號問題變形
3. 學習更多 Stack 的應用場景
