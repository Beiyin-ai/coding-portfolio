from typing import List

class Solution:
    def restoreString_dict(self, s: str, indices: List[int]) -> str:
        """ 重新排列字串
        
        解法一：使用字典建立索引到字元的映射
        我的第一次解法
        """
        sMap = {}
        result = ""
        for i in range(len(s)):
            sMap[i] = s[i]          # 建立索引到字元的映射
        for j in indices:
            result += sMap[j]       # 按 indices 的順序取字元
        return result

    def restoreString_array(self, s: str, indices: List[int]) -> str:
        """ 重新排列字串
        
        解法二：直接使用數組操作
        我的第二種解法，更高效
        """
        result = [''] * len(s)      # 建立一個固定長度的空陣列
        for i, char in enumerate(s):
            result[indices[i]] = char   # 把字元放到指定位置
        return ''.join(result)      # 合併成字串

    # LeetCode 要求的函數名稱
    def restoreString(self, s: str, indices: List[int]) -> str:
        # 使用第二種解法作為主要解法
        return self.restoreString_array(s, indices)

# 測試程式碼
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("codeleet", [4,5,6,7,0,2,1,3], "leetcode"),
        ("abc", [0,1,2], "abc"),
        ("aiohn", [3,1,4,2,0], "nihao"),
    ]
    
    print("測試結果：")
    print("解法一（字典映射）：")
    for i, (s, indices, expected) in enumerate(test_cases, 1):
        result = solution.restoreString_dict(s, indices)
        status = "✓" if result == expected else "✗"
        print(f"  測試 {i}: {s} → {result} {status}")
    
    print("\n解法二（數組操作）：")
    for i, (s, indices, expected) in enumerate(test_cases, 1):
        result = solution.restoreString_array(s, indices)
        status = "✓" if result == expected else "✗"
        print(f"  測試 {i}: {s} → {result} {status}")
