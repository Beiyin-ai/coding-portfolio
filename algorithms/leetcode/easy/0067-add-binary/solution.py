class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """ 二進位字串相加
        
        模擬手工二進位加法，從最低位開始逐位計算
        這是我的解法，清晰直觀且效率良好
        """
        i, j = len(a) - 1, len(b) - 1
        carry = 0  # 進位
        result = []

        while i >= 0 or j >= 0 or carry:
            # 取得當前位數，如果索引為負則為0
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            total = digit_a + digit_b + carry
            result.append(str(total % 2))   # 當前位元
            carry = total // 2              # 更新進位

            i -= 1
            j -= 1

        # 結果是從低位到高位建立的，需要反轉
        return ''.join(reversed(result))
