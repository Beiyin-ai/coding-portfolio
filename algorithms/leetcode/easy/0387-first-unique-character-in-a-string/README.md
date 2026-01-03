# 387. First Unique Character in a String

**難度：** Easy  
**標籤：** Hash Table, String  
**連結：** [LeetCode 387](https://leetcode.com/problems/first-unique-character-in-a-string/)

## 題目描述
Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

### 範例
**範例 1：**
```
Input: s = "leetcode"
Output: 0
Explanation: The character 'l' at index 0 is the first character that does not occur at any other index.
```

**範例 2：**
```
Input: s = "loveleetcode"
Output: 2
```

**範例 3：**
```
Input: s = "aabb"
Output: -1
```

### 限制條件
- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters.

## 解法 1：我的新解法（使用 Counter）

### 程式碼
```python
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        
        for key, value in count.items():
            if value == 1:
                return s.index(key)
        
        return -1
```

### 解題思路
1. **統計頻率**：使用 `Counter` 快速統計每個字符出現次數
2. **遍歷字典**：使用 `items()` 方法遍歷字符和頻率
3. **找到第一個唯一字符**：當頻率為 1 時，返回該字符在原始字串中的索引
4. **返回 -1**：如果沒有唯一字符，返回 -1

### 優點
- **使用 Python 標準庫**：`Counter` 比手動統計更簡潔
- **邏輯清晰**：直接遍歷計數字典，意圖明確
- **可讀性高**：程式碼更容易理解

## 解法 2：我原本的解法（手動統計）

### 程式碼
```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1
```

### 解題思路
1. **手動統計頻率**：使用字典手動計算每個字符出現次數
2. **第二次遍歷**：按照原始順序檢查每個字符的頻率
3. **找到第一個唯一字符**：當頻率為 1 時，返回索引
4. **返回 -1**：如果沒有找到，返回 -1

### 解題思路比較
| 方法 | 程式碼長度 | 可讀性 | Python 技巧 | 學習價值 |
|------|-----------|--------|-------------|----------|
| 新解法（Counter） | 較短 | 高 | 使用標準庫 | 學習 Python 內建工具 |
| 原本解法（手動統計） | 較長 | 中等 | 基礎字典操作 | 學習基礎演算法 |

### 複雜度分析
- **時間複雜度：O(n)**
  - 兩種解法都是 O(n)，需要遍歷字串統計頻率
  - 新解法中 `Counter` 的實作也是 O(n)
- **空間複雜度：O(1)**
  - 只使用固定大小的字典（最多 26 個小寫字母）

### 測試範例
```python
測試 1: "leetcode" → 0
測試 2: "loveleetcode" → 2
測試 3: "aabb" → -1
測試 4: "abcabc" → -1
測試 5: "z" → 0
```

### 學習心得
這題讓我學到：
1. **善用標準庫**：`Counter` 比手動統計更簡潔高效
2. **不同遍歷方式**：`items()` 遍歷 vs 索引遍歷
3. **程式碼優化**：從基礎實現進步到使用內建工具
4. **效能考量**：雖然時間複雜度相同，但程式碼可讀性更重要

### 相關題目
- [451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) (Medium)
- [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome/) (Easy)
- [383. Ransom Note](https://leetcode.com/problems/ransom-note/) (Easy)

### 下一步計畫
1. 嘗試用其他方法解決（如固定長度數組）
2. 練習更多字串處理相關題目
3. 學習更多 Python collections 模組的使用
