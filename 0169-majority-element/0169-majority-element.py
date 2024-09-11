class Solution(object):
    def majorityElement(self, nums):
        x = Counter(nums)
        res = max(x, key = x.get)
        return res