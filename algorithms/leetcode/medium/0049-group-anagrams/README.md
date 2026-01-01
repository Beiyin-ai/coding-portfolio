# 49. Group Anagrams

**難度：** Medium  
**標籤：** Hash Table, String, Sorting  
**連結：** [LeetCode 49](https://leetcode.com/problems/group-anagrams/)

## 題目描述
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

### 範例
**範例 1：**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
- "bat" 沒有其他字母異位詞
- "nat" 和 "tan" 是字母異位詞
- "ate", "eat", "tea" 是字母異位詞
```

**範例 2：**
```
Input: strs = [""]
Output: [[""]]
```

**範例 3：**
```
Input: strs = ["a"]
Output: [["a"]]
```

### 限制條件
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## 解法：使用排序作為 Key（我的解法）

### 程式碼
```python
class Solution:
    def groupAnagrams(self, strs):
        group = {}
        for s in strs:
            keys = "".join(sorted(s))
            if keys not in group:
                group[keys] = []
            group[keys].append(s)
        return list(group.values())
```

### 解題思路
1. **核心觀察**：字母異位詞排序後會得到相同的字串
2. **建立 HashMap**：使用排序後的字串作為 key
3. **分組儲存**：將原始字串存入對應的 key 中
4. **返回結果**：將 HashMap 的值轉為 list

### 我的思考過程
我想到 Valid Anagram 那題學到的技巧：字母異位詞排序後會相同
所以可以用排序後的字串作為識別 key
用 HashMap 來分組收集相同 key 的字串

### 關鍵點
- **排序作為 key**：這是識別字母異位詞最直接的方法
- **HashMap 的使用**：Python 中可以用 dict 儲存分組
- **邊界條件**：
  - 空字串：排序後仍是空字串，自成一群組
  - 單一字元：排序後不變
  - 所有字串長度為 0：全部歸為同一群組

### 複雜度分析
- **時間複雜度：O(n * k log k)**
  - `n`：字串數量
  - `k`：字串平均長度
  - 每個字串需要 O(k log k) 時間排序
- **空間複雜度：O(n * k)**
  - 需要儲存所有字串的排序版本和原始版本

### 測試範例
```python
測試 1: ["eat","tea","tan","ate","nat","bat"]
→ [["bat"],["nat","tan"],["ate","eat","tea"]]

測試 2: [""]
→ [[""]]

測試 3: ["a"]
→ [["a"]]

測試 4: ["abc","bca","cab","def","fed"]
→ [["def","fed"],["abc","bca","cab"]]
```

### 學習心得
這題是 Valid Anagram 的進階應用。我學到：
1. **活用已學技巧**：把 Valid Anagram 的判斷方法用來分組
2. **HashMap 的靈活應用**：可以用各種形式的資料作為 key
3. **從簡單到複雜**：從判斷兩個字串是否為字母異位詞，到分組多個字串

這是我的第一個 Medium 題目，讓我更有信心挑戰更難的題目！

### 相關題目
- [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) (Easy) - 我已經解過這題
- [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) (Medium)

### 下一步計畫
1. 繼續挑戰更多 Medium 題目
2. 嘗試用不同方法解決同一問題
3. 學習更多資料結構的應用
