from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        找出出現頻率最高的 k 個元素
        
        我的解法：使用 collections.Counter 的 most_common 方法
        簡單直接，充分利用 Python 內建函式
        """
        # 統計每個數字的出現頻率
        dict_nums = Counter(nums)
        
        # 取得出現頻率最高的 k 個元素
        most_common_nums = dict_nums.most_common(k)
        
        # 提取數字部分（不需要頻率）
        result = []
        for items in most_common_nums:
            result.append(items[0])
            
        return result
