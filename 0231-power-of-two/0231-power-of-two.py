class Solution(object):
    def isPowerOfTwo(self, n):
        if n & (n-1) == 0 and n > 0:
            return True
        return False
        