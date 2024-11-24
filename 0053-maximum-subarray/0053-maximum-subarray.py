class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = nums[0]
        max_ele = nums[0]

        for i in range(1,len(nums)):
            max_value = max(nums[i], max_value+nums[i])
            max_ele = max(max_ele, max_value)

        return max_ele