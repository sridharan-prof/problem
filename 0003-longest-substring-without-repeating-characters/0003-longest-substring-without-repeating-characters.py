class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        n = len(s)
        max_sum = 0
        for i in range(n):
            if s[i] in res:
                while s[i] in res:
                    res.pop(0)
            res.append(s[i])
            max_sum = max(max_sum, len(res))
        return max_sum

        
        