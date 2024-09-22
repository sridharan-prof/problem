class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums) + 1
        print(length)
        for i in range(length):
            if i not in nums:
                return i