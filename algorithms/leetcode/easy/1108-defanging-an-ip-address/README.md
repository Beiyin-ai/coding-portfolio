1108. Defanging an IP Address
完成日期： 2026-01-23
難度： Easy
標籤： String
連結： LeetCode 1108

## 題目描述
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

## 範例
**範例 1：**
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

**範例 2：**
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

## 限制條件
- The given address is a valid IPv4 address.

## 解法：直接替換（我的解法）
### 程式碼
```python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        """ IP 地址去範圍化

        使用 Python 內建的 replace() 方法
        將所有的 '.' 替換為 '[.]'
        這是我的解法，一行解決
        """
        return address.replace('.', '[.]')
```

### 解題思路
1. **讀取輸入**：取得 IPv4 地址字串
2. **字串替換**：使用 `replace()` 方法將所有的句點替換為 "[.]"
3. **返回結果**：返回替換後的字串

## 我的思考過程
1. **問題分析**：這是一道簡單的字串處理題目，需要將 IP 地址中的點替換為特定的格式
2. **方法選擇**：Python 的 `replace()` 方法是處理這種問題最直接的方式
3. **實現考慮**：
   - 確認 `replace()` 會替換所有出現的點，而不僅僅是第一個
   - 確認替換格式是 "[.]" 而不是其他格式
4. **邊界情況**：
   - IP 地址長度在 7-15 個字元之間
   - 總是有效的 IPv4 地址

## 關鍵點
- **字串操作**：熟悉 Python 的字串內建方法
- **替換規則**：將 "." 替換為 "[.]" 而不是其他格式
- **效能考慮**：`replace()` 方法通常比手動遍歷更高效
- **IP 地址格式**：了解 IPv4 地址的基本格式

## 複雜度分析
- **時間複雜度**：O(n)
  - `replace()` 方法需要遍歷整個字串
  - 其中 n 是字串長度
- **空間複雜度**：O(n)
  - 創建了新的字串來儲存替換結果

## 測試範例
**測試 1**：address = "1.1.1.1"
→ 替換過程："1.1.1.1" → "1[.]1[.]1[.]1"

**測試 2**：address = "255.100.50.0"
→ 替換過程："255.100.50.0" → "255[.]100[.]50[.]0"

**測試 3**：address = "0.0.0.0"
→ 替換過程："0.0.0.0" → "0[.]0[.]0[.]0"

**測試 4**：address = "192.168.1.1"
→ 替換過程："192.168.1.1" → "192[.]168[.]1[.]1"

## 學習心得
這題讓我學到：
1. **Python 字串方法**：熟練使用 `replace()` 等內建方法
2. **問題簡化**：看似需要複雜處理的問題，可能只需要簡單的字串操作
3. **效能比較**：不同解法的時間和空間複雜度分析
4. **代碼簡潔性**：一行代碼可以解決的問題，不需要複雜的實現
5. **IP 地址知識**：IPv4 地址的基本格式和結構

## 相關題目
- 58. Length of Last Word (Easy) - 字串處理
- 387. First Unique Character in a String (Easy) - 字串遍歷
- 344. Reverse String (Easy) - 字串操作
- 151. Reverse Words in a String (Medium) - 進階字串處理

## 下一步計畫
- 嘗試更多字串處理相關的題目
- 學習正則表達式在字串處理中的應用
- 挑戰中等難度的字串問題
