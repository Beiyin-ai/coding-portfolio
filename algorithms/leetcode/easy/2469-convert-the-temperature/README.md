2469. Convert the Temperature
完成日期： 2026-01-22
難度： Easy
標籤： Math
連結： LeetCode 2469

## 題目描述
You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

Return the array ans. Answers within 10^-5 of the actual answer will be accepted.

Note that:
- Kelvin = Celsius + 273.15
- Fahrenheit = Celsius * 1.80 + 32.00

## 範例
**範例 1：**
Input: celsius = 36.50
Output: [309.65000, 97.70000]
Explanation: Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.

**範例 2：**
Input: celsius = 122.11
Output: [395.26000, 251.79800]
Explanation: Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in Fahrenheit is 251.798.

## 限制條件
- 0 <= celsius <= 1000

## 解法：直接計算（我的解法）
### 程式碼
```python
from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        """ 溫度轉換
        
        根據公式直接計算 Kelvin 和 Fahrenheit
        這是我的解法，簡單直接
        """
        ans = []

        # 計算 Kelvin
        kelvin = celsius + 273.15
        ans.append(kelvin)
        
        # 計算 Fahrenheit
        fahrenheit = celsius * 1.80 + 32.00
        ans.append(fahrenheit)

        return ans
```

### 解題思路
1. **讀取輸入**：取得攝氏溫度值
2. **應用公式**：
   - Kelvin = Celsius + 273.15
   - Fahrenheit = Celsius × 1.80 + 32.00
3. **儲存結果**：將計算結果放入列表
4. **返回結果**：返回包含兩個溫度的列表

## 我的思考過程
1. **問題分析**：這是一道簡單的數學計算題，直接應用公式即可
2. **公式確認**：確認題目給出的轉換公式正確無誤
3. **實現選擇**：使用最直接的方法，一步步計算
4. **邊界檢查**：攝氏溫度為非負數，且範圍在 0 到 1000 之間
5. **精度考慮**：使用浮點數計算，Python 的浮點數精度足夠

## 關鍵點
- **公式應用**：直接使用題目提供的轉換公式
- **浮點數計算**：Python 的浮點數運算
- **列表操作**：使用 `append()` 方法添加元素
- **返回值格式**：必須返回 `[kelvin, fahrenheit]` 格式的列表
- **精度要求**：答案誤差在 10^-5 內即可接受

## 複雜度分析
- **時間複雜度**：O(1)
  - 只有常數次運算
  - 與輸入大小無關
- **空間複雜度**：O(1)
  - 只使用了固定大小的變數
  - 返回的列表大小固定為 2

## 測試範例
**測試 1**：celsius = 36.50
→ 計算過程：
  kelvin = 36.50 + 273.15 = 309.65
  fahrenheit = 36.50 × 1.80 + 32.00 = 65.70 + 32.00 = 97.70
→ 結果：[309.65000, 97.70000]

**測試 2**：celsius = 122.11
→ 計算過程：
  kelvin = 122.11 + 273.15 = 395.26
  fahrenheit = 122.11 × 1.80 + 32.00 = 219.798 + 32.00 = 251.798
→ 結果：[395.26000, 251.79800]

**測試 3**：celsius = 0
→ 計算過程：
  kelvin = 0 + 273.15 = 273.15
  fahrenheit = 0 × 1.80 + 32.00 = 32.00
→ 結果：[273.15000, 32.00000]

**測試 4**：celsius = 100
→ 計算過程：
  kelvin = 100 + 273.15 = 373.15
  fahrenheit = 100 × 1.80 + 32.00 = 180.00 + 32.00 = 212.00
→ 結果：[373.15000, 212.00000]

**測試 5**：celsius = -40（注意：題目限制 celsius >= 0，此為額外測試）
→ 有趣的巧合：-40°C = -40°F
→ kelvin = -40 + 273.15 = 233.15

## 學習心得
這題讓我學到：
1. **簡單問題的重要性**：即使是簡單題目，也能練習基本語法和思考
2. **公式轉換**：溫度單位轉換的實際應用
3. **浮點數精度**：理解浮點數計算的精度問題
4. **問題閱讀**：仔細閱讀題目要求和限制條件
5. **程式結構**：即使是簡單問題，也要保持程式碼清晰易讀

## 相關題目
- 13. Roman to Integer (Easy) - 另一種數值轉換問題
- 67. Add Binary (Easy) - 二進位計算
- 50. Pow(x, n) (Medium) - 數學計算
- 69. Sqrt(x) (Easy) - 數學函數

## 下一步計畫
- 嘗試更複雜的數學計算題目
- 練習浮點數精度處理的相關題目
- 學習數值計算的最佳實踐
