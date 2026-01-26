168. Excel Sheet Column Title
完成日期： 2026-01-26
難度： Easy
標籤： Math, String
連結： LeetCode 168

## 題目描述
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:
- A -> 1
- B -> 2
- C -> 3
- ...
- Z -> 26
- AA -> 27
- AB -> 28
- ...

## 範例
**範例 1：**
```
Input: columnNumber = 1
Output: "A"
```

**範例 2：**
```
Input: columnNumber = 28
Output: "AB"
```

**範例 3：**
```
Input: columnNumber = 701
Output: "ZY"
```

## 限制條件
- 1 <= columnNumber <= 2^31 - 1

## 解法：26進位制轉換（我的解法）
### 程式碼
```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """ Excel 列標題轉換

        關鍵在於 Excel 使用的是 1-based 26進位制
        需要將 columnNumber 轉換為 0-based 才能正確計算
        這是我的解法
        """
        result = []
        while columnNumber > 0:
            columnNumber -= 1  # 調整成 0-based
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(reversed(result))
```

### 解題思路
1. **理解問題**：Excel 列標題是 1-based 26進位制（A=1, Z=26, AA=27）
2. **關鍵調整**：將輸入的 columnNumber 減 1 轉為 0-based
3. **進位轉換**：使用 26 進位制轉換，每次取餘數對應到字母
4. **逆序處理**：因為是從低位到高位計算，最後需要反轉

### 詳細步驟
以 columnNumber = 28 為例：
1. 28 - 1 = 27 (轉為 0-based)
2. 27 % 26 = 1 → B (0→A, 1→B)
3. 27 // 26 = 1
4. 1 - 1 = 0 (轉為 0-based)
5. 0 % 26 = 0 → A
6. 0 // 26 = 0 (結束)
7. 結果 [B, A] → 反轉 → [A, B] → "AB"

## 我的思考過程
### 第一階段：理解問題
1. **觀察規律**：
   - A=1, B=2, ..., Z=26
   - AA=27, AB=28, ..., AZ=52, BA=53
2. **發現特點**：類似 26 進位制，但不是標準的 0-based
3. **關鍵困惑**：為什麼 Z(26) 後面是 AA(27) 而不是 BA？

### 第二階段：分析問題
1. **嘗試對比**：與正常的 26 進位制比較：
   - 正常: 0=A, 1=B, ..., 25=Z, 26=AA, 27=AB
   - Excel: 1=A, 2=B, ..., 26=Z, 27=AA, 28=AB
2. **關鍵發現**：Excel 系統是 1-based，需要減 1 轉為 0-based
3. **數學關係**：columnNumber - 1 = Σ(數字_i × 26^i)

### 第三階段：實現解法
1. **核心操作**：每次循環時先減 1，再取餘數和商
2. **字元轉換**：使用 `chr(餘數 + ord('A'))` 轉為字母
3. **結果處理**：因為先得到的是低位字母，需要反轉

## 關鍵點
### 1. 1-based vs 0-based
- **正常數值系統**：0-based (0, 1, 2, ...)
- **Excel 系統**：1-based (1, 2, 3, ...)
- **轉換關鍵**：`columnNumber -= 1`

### 2. 字母轉換
- A-Z 對應 0-25
- 使用 `chr()` 和 `ord()` 進行轉換
- `ord('A') = 65`, `ord('Z') = 90`

### 3. 進位制處理
- 類似 10 進位轉 2 進位，但是 26 進位
- 取餘數得到當前位的字母
- 除以 26 進入下一位

## 複雜度分析
### 時間複雜度：O(log₂₆ n)
- 每次循環 columnNumber 除以 26
- 循環次數約為 log₂₆(columnNumber)
- 對於最大輸入 2^31-1 ≈ 2.1×10^9，循環約 7 次

### 空間複雜度：O(log₂₆ n)
- 儲存結果的字串長度
- 約為 log₂₆(columnNumber)

## 測試範例
### 基礎測試
1. **1 → A**
   - 1-1=0, 0%26=0→A, 0//26=0 → A

2. **26 → Z**
   - 26-1=25, 25%26=25→Z, 25//26=0 → Z

3. **27 → AA**
   - 27-1=26, 26%26=0→A, 26//26=1
   - 1-1=0, 0%26=0→A, 0//26=0 → AA

### 進階測試
4. **28 → AB**（範例）
   - 28-1=27, 27%26=1→B, 27//26=1
   - 1-1=0, 0%26=0→A, 0//26=0 → AB

5. **701 → ZY**（範例）
   - 701-1=700, 700%26=24→Y, 700//26=26
   - 26-1=25, 25%26=25→Z, 25//26=0 → ZY

6. **702 → ZZ**
   - 702-1=701, 701%26=25→Z, 701//26=26
   - 26-1=25, 25%26=25→Z, 25//26=0 → ZZ

7. **703 → AAA**
   - 703-1=702, 702%26=0→A, 702//26=27
   - 27-1=26, 26%26=0→A, 26//26=1
   - 1-1=0, 0%26=0→A, 0//26=0 → AAA

## 常見錯誤
### 錯誤 1：忘記減 1
```python
# 錯誤寫法
while columnNumber > 0:
    result.append(chr(columnNumber % 26 + ord('A') - 1))  # 會出錯
    columnNumber //= 26
```
**問題**：當 columnNumber=26 時，26%26=0，0+65-1=64 → '@' 而不是 'Z'

### 錯誤 2：在錯誤的地方減 1
```python
# 錯誤寫法
while columnNumber > 0:
    result.append(chr((columnNumber - 1) % 26 + ord('A')))
    columnNumber //= 26  # 這裡忘記處理減 1 後的影響
```
**問題**：除法應該在減 1 之前進行

## 學習心得
這題讓我學到：
1. **1-based 系統**：理解 Excel 列標題的 1-based 特性
2. **進位制轉換**：掌握任意進位制的轉換方法
3. **邊界條件**：處理 Z→AA 的特殊情況
4. **問題分析**：從具體例子中找出數學規律
5. **代碼優化**：使用列表和 `join()` 提高效能

## 相關題目
- **171. Excel Sheet Column Number** (Easy) - 反向問題
- **273. Integer to English Words** (Hard) - 更複雜的數字轉文字
- **12. Integer to Roman** (Medium) - 數字轉羅馬數字
- **504. Base 7** (Easy) - 進位制轉換

## 下一步計畫
1. 嘗試 **171. Excel Sheet Column Number**（反向問題）
2. 練習更多進位制轉換的題目
3. 學習處理邊界條件的技巧
