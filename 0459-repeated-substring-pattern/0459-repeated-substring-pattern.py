class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        double_s = (s + s)[1:-1]
        return s in double_s
        