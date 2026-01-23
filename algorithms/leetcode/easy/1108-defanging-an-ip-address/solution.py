class Solution:
    def defangIPaddr(self, address: str) -> str:
        """ IP 地址去範圍化
        
        使用 Python 內建的 replace() 方法
        將所有的 '.' 替換為 '[.]'
        這是我的解法，一行解決
        """
        return address.replace('.', '[.]')
