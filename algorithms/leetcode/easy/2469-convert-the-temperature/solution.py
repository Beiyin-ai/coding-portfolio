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
