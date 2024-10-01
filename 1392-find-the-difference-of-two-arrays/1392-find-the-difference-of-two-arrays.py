class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
        num1 = set(nums1)
        num2 = set(nums2)

        res1 = list(num1 - num2)
        res2 = list(num2 - num1)
        return [res1,res2]