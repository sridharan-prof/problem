class Solution(object):
    def productExceptSelf(self, nums):
        pre = 1
        post = 1
        new = [0] * (len(nums))
        
        for i in range(len(nums)):
            new[i] = pre
            pre *= nums[i]
        for i in range(len(nums)-1, -1, -1): 
            new[i] *= post
            post *= nums[i]
        return new