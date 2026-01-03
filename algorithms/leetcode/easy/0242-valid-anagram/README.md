# 242. Valid Anagram

**完成日期：** 2025-12-29  

## 學習歷程
這題記錄了我從基礎解法到優化解法的學習過程！

## 解法 1：排序法（我的第一個想法）

### 程式碼
```python
def isAnagram_sorted(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```

### 解題思路
1. 將兩個字串分別排序
2. 比較排序後的結果是否相同
3. 如果相同，表示是易位構詞（anagram）

### 複雜度分析
- **時間複雜度：O(n log n)**，排序需要 O(n log n) 時間
- **空間複雜度：O(n)**，需要儲存排序後的字串

### 學習心得
這是我第一個想到的解法，直觀但效率不是最佳。

## 解法 2：Counter 法（學習後改進）

### 程式碼
```python
from collections import Counter

def isAnagram_counter(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
```

### 解題思路
1. 使用 Python 的 `collections.Counter` 計數字元出現次數
2. 比較兩個字串的字元計數是否完全相同
3. Counter 會自動處理字元頻率的比較

### 複雜度分析
- **時間複雜度：O(n)**，只需要遍歷字串一次
- **空間複雜度：O(k)**，k 是字符集大小（英文小寫字母為 26）

### 學習心得
學習到 Python 內建的 `Counter` 工具，讓程式碼更簡潔，效率也更好！

## 解法 3：陣列計數法（手動實現）

### 程式碼
```python
def isAnagram_array(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count = [0] * 26
    for char in s:
        count[ord(char) - ord("a")] += 1
    for char in t:
        count[ord(char) - ord("a")] -= 1
        if count[ord(char) - ord("a")] < 0:
            return False
    return True
```

### 解題思路
1. 如果長度不同直接返回 False
2. 建立長度 26 的陣列（對應 a-z）
3. 遍歷第一個字串，增加計數
4. 遍歷第二個字串，減少計數
5. 如果任何計數變負數，返回 False

### 複雜度分析
- **時間複雜度：O(n)**，只需要遍歷字串兩次
- **空間複雜度：O(1)**，只使用固定大小的陣列

### 學習心得
手動實現計數器幫助我理解 `Counter` 的底層原理，也學到字元到索引的轉換技巧。

## 測試結果
所有測試案例都通過！✓

## 學習總結
1. **從簡單到優化**：排序法 → Counter 法 → 陣列法
2. **工具學習**：學到 Python 內建 `Counter` 的強大功能
3. **原理理解**：手動實現幫助理解底層機制
4. **複雜度分析**：O(n log n) → O(n) → O(n) 的時間複雜度進步
