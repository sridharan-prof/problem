class Solution:
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        x = self.gcd(len(str1), len(str2))
        return str1[:x]
    
    def gcd(self, a, b):
        res = min(a, b)
        while res:
            if a % res == 0 and b % res == 0:
                break
            res -= 1
        return res

        