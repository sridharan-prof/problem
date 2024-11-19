class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cur = 0
        prev = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
            else:
                ans = max(ans,cur+prev)
                prev = cur
                cur = 0
        ans = max(ans, prev+cur)
        return ans-1 if ans == len(nums) else ans  
        