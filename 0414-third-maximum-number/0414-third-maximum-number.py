class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = set(nums)
        if len(n) < 3:
            return max(nums)
        else:
            res = sorted(n, reverse = True)
            return res[2]
            