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


# 測試程式碼
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        (1, "A"),
        (26, "Z"),
        (27, "AA"),
        (28, "AB"),
        (52, "AZ"),
        (53, "BA"),
        (701, "ZY"),
        (702, "ZZ"),
        (703, "AAA"),
        (18278, "ZZZ"),
        (18279, "AAAA"),
    ]
    
    print("Excel Sheet Column Title 測試結果：")
    print("=" * 40)
    
    all_passed = True
    for i, (input_num, expected) in enumerate(test_cases, 1):
        result = solution.convertToTitle(input_num)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        
        print(f"測試 {i:2d}: {input_num:6d} → {result:8s} {status} (預期: {expected})")
    
    print("=" * 40)
    if all_passed:
        print("✅ 所有測試通過！")
    else:
        print("❌ 有測試失敗！")
    
    # 額外：顯示一些有趣的例子
    print("\n有趣的例子：")
    interesting_cases = [(1, "A"), (26, "Z"), (27, "AA"), (702, "ZZ"), (703, "AAA")]
    for num, title in interesting_cases:
        print(f"  {num:6d} → {title}")
