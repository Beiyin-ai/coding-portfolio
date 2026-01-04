"""
LeetCode 643. Maximum Average Subarray I

解法一：雙指針滑動窗口（我的初始解法）
時間複雜度：O(n)
空間複雜度：O(1)

解法二：優化的滑動窗口（學到的新解法）
時間複雜度：O(n)
空間複雜度：O(1)

解題歷程：
1. 一開始我用雙指針的方式實現滑動窗口
2. 後來學到更優雅的方法：先計算第一個窗口，然後減左加右
3. 兩種解法時間複雜度相同，但第二種更簡潔
"""

from typing import List

class Solution:
    def findMaxAverage_original(self, nums: List[int], k: int) -> float:
        """
        解法一：雙指針滑動窗口（我的初始解法）
        
        思路：
        1. 用 left 和 right 兩個指針定義窗口
        2. right 向右移動，累加元素值
        3. 當窗口大小達到 k 時，更新最大總和
        4. 移動窗口：減去 nums[left]，left 向右移動
        
        優點：直觀，容易理解滑動窗口的概念
        缺點：需要條件判斷窗口大小
        """
        left = 0
        total = 0
        max_value = float('-inf')

        for right in range(len(nums)):
            total += nums[right]

            if right - left + 1 == k:
                max_value = max(max_value, total)
                total -= nums[left]
                left += 1

        return max_value / k
    
    def findMaxAverage_optimized(self, nums: List[int], k: int) -> float:
        """
        解法二：優化的滑動窗口（學到的新解法）
        
        思路：
        1. 先計算第一個窗口的總和
        2. 從第 k 個元素開始，每次減去左邊元素，加上右邊元素
        3. 更新最大總和
        
        優點：
        - 更簡潔，不需要兩個指針
        - 不需要條件判斷
        - 邏輯更清晰：明確的「減左加右」操作
        
        學習點：有時候先計算初始狀態，再進行迭代會更簡單
        """
        window_sum = sum(nums[:k])
        max_values = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_values = max(max_values, window_sum)

        return max_values / k
    
    # 主要方法，使用優化解法
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """對外接口，使用優化解法"""
        return self.findMaxAverage_optimized(nums, k)


# 測試程式碼
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1,12,-5,-6,50,3], 4, 12.75),  # 範例 1
        ([5], 1, 5.0),                  # 範例 2
        ([0,4,0,3,2], 1, 4.0),         # 簡單測試
        ([1,2,3,4,5], 3, 4.0),         # 遞增數組
        ([-1,-2,-3,-4,-5], 2, -1.5),   # 負數測試
    ]

    print("=== Maximum Average Subarray I 測試 ===")
    print("兩種解法比較測試\n")
    
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        # 測試兩種解法
        result1 = solution.findMaxAverage_original(nums, k)
        result2 = solution.findMaxAverage_optimized(nums, k)
        
        # 檢查結果是否一致
        same_result = abs(result1 - result2) < 1e-10
        
        # 檢查是否與預期相符（允許計算誤差）
        correct1 = abs(result1 - expected) < 1e-5
        correct2 = abs(result2 - expected) < 1e-5
        
        print(f"測試 {i}:")
        print(f"  輸入: nums = {nums}, k = {k}")
        print(f"  預期: {expected}")
        print(f"  解法一結果: {result1:.5f} {'✓' if correct1 else '✗'}")
        print(f"  解法二結果: {result2:.5f} {'✓' if correct2 else '✗'}")
        print(f"  兩種解法結果一致: {'✓' if same_result else '✗'}")
        
        # 顯示兩種解法的差異
        if not same_result:
            print(f"  差異: {abs(result1 - result2):.10f}")
        
        print()
    
    print("總結：")
    print("1. 兩種解法都能得到正確答案")
    print("2. 解法二更簡潔高效")
    print("3. 解法一有助於理解滑動窗口的基本概念")
