class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        lst = ["a","e","i","o","u"]
        count = 0
        max_count = 0
        for i in range(k):
            if s[i] in lst:
                count += 1
        max_count = count
        for i in range(k,len(s)):
            if s[i-k] in lst:
                count -= 1
            if s[i] in lst:
                count += 1
                max_count = max(count,max_count)
        return max_count
 
        