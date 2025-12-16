# 1480. Running Sum of 1d Array
# 解題日期: 13天前

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = 0
        outputList = []
        for num in nums:
            output += num
            outputList.append(output)
        return outputList
