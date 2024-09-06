class Solution(object):
    def isSubsequence(self, s, t):
        sp = 0
        s_len = len(s)

        for i in t:
            if sp < s_len and i == s[sp]:
                sp += 1
        return sp == s_len