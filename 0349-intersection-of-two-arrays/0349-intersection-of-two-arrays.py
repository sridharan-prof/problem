class Solution(object):
    def intersection(self, nums1, nums2):
        x = set(nums1)
        y = set(nums2)
        res = list(x & y)
        return res