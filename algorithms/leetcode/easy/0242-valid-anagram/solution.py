# 242. Valid Anagram

from collections import Counter

class Solution:
    def isAnagram_sorted(self, s: str, t: str) -> bool:
        """排序解法：比較排序後的字串"""
        return sorted(s) == sorted(t)

    def isAnagram_counter(self, s: str, t: str) -> bool:
        """Counter解法：計數字元出現次數"""
        return Counter(s) == Counter(t)

    def isAnagram_array(self, s: str, t: str) -> bool:
        """陣列計數解法：手動實現計數"""
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

    # LeetCode 要求的方法
    def isAnagram(self, s: str, t: str) -> bool:
        return self.isAnagram_counter(s, t)

# 測試程式碼
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("anagram", "nagaram"),
        ("rat", "car"),
        ("", ""),
        ("a", "a"),
        ("abc", "cba")
    ]

    print("=== Valid Anagram 測試 ===")
    print(f"解法 1：排序法 (O(n log n))")
    print(f"解法 2：Counter法 (O(n))")
    print(f"解法 3：陣列法 (O(n))\n")

    for s, t in test_cases:
        result1 = solution.isAnagram_sorted(s, t)
        result2 = solution.isAnagram_counter(s, t)
        result3 = solution.isAnagram_array(s, t)

        all_same = result1 == result2 == result3
        status = "✓" if all_same else "✗"

        print(f"測試: {status}")
        print(f"  輸入: s=\"{s}\", t=\"{t}\"")
        print(f"  排序法: {result1}")
        print(f"  Counter法: {result2}")
        print(f"  陣列法: {result3}")
        print()
