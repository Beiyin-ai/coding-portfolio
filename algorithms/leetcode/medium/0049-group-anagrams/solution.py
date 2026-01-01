class Solution:
    def groupAnagrams(self, strs):
        """
        將字母異位詞分組

        使用排序後的字串作為 key 來分組
        這是我的解法，簡單直觀
        """
        group = {}
        for s in strs:
            keys = "".join(sorted(s))
            if keys not in group:
                group[keys] = []
            group[keys].append(s)
        return list(group.values())
