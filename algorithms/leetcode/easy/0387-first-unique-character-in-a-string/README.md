# 387. First Unique Character in a String

## 解法 1：使用 HashMap 統計頻率（我的解法）

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
1. **第一次遍歷**：使用 HashMap 統計每個字符出現的頻率
2. **第二次遍歷**：按照原始順序檢查每個字符，找到第一個頻率為 1 的字符
3. **返回結果**：如果找到則返回索引，否則返回 -1

### 關鍵點
- 需要**兩次遍歷**：第一次統計頻率，第二次找第一個唯一字符
- 由於只有小寫英文字母，HashMap 的大小最多 26，空間複雜度為 O(1)
- 使用  可以同時獲取索引和字符，但我選擇用  保持清晰

### 複雜度分析
- **時間複雜度：O(n)** - 兩次線性遍歷，n 為字串長度
- **空間複雜度：O(1)** - 只有 26 個小寫字母，HashMap 大小固定

### 學習心得
這題幫助我複習了 HashMap 的基本操作。我學習到的重點：
1. **統計頻率**是處理字串問題的常見技巧
2. 有時候需要**兩次遍歷**才能同時滿足「統計」和「順序」的要求
3. 在 Python 中， 可以讓程式碼更簡潔，但用  對初學者更直觀
4. 這題的變形可以問「最後一個唯一字符」或「所有唯一字符」，解法類似

### 測試範例


### 其他解法
#### 解法 2：使用 collections.Counter（更簡潔）
```python
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1
```

#### 解法 3：使用固定數組（最優化）
```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 創建長度為 26 的數組來統計每個字母的出現次數
        freq = [0] * 26
        
        # 第一次遍歷：統計頻率
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        # 第二次遍歷：找第一個唯一字符
        for i, char in enumerate(s):
            if freq[ord(char) - ord('a')] == 1:
                return i
        
        return -1
```

### 下一步計畫
1. 嘗試用其他語言實現（如 Kotlin）
2. 解相關的變形題目
3. 學習更高效的字串處理技巧
