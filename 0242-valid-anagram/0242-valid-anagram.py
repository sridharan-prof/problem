class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        x = list(s)
        y = list(t)
        if len(x) != len(y):
            return False
        return sorted(x) == sorted(y)