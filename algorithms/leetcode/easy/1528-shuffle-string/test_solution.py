"""
1528. Shuffle String - 測試檔案
測試不同解法的效能
"""
import time
from solution import Solution

def test_performance():
    """測試兩種解法的效能"""
    solution = Solution()
    
    # 建立測試數據
    s = "abcdefghijklmnopqrstuvwxyz" * 100  # 2600個字元
    indices = list(range(len(s)))
    # 將 indices 隨機打亂
    import random
    random.shuffle(indices)
    
    print("效能測試（字串長度：{}）".format(len(s)))
    print("=" * 50)
    
    # 測試解法一
    start_time = time.time()
    result1 = solution.restoreString_dict(s, indices)
    time1 = time.time() - start_time
    
    # 測試解法二
    start_time = time.time()
    result2 = solution.restoreString_array(s, indices)
    time2 = time.time() - start_time
    
    # 驗證結果是否相同
    if result1 == result2:
        print("✅ 兩種解法結果一致")
    else:
        print("❌ 兩種解法結果不同")
    
    print("\n效能比較：")
    print(f"解法一（字典映射）：{time1:.6f} 秒")
    print(f"解法二（數組操作）：{time2:.6f} 秒")
    print(f"效能提升：{(time1 - time2) / time1 * 100:.1f}%")
    
    return time1, time2

if __name__ == "__main__":
    test_performance()
