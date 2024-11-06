class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        zeros = 0
        maxlength = 0

        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                length = r - l + 1
                maxlength = max(maxlength, length)
            r += 1
        return maxlength