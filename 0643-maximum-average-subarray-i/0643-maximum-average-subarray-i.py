class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        max_window = window
        n = len(nums)
        for i in range(0,n-k):
            window += nums[i+k] - nums[i]
            max_window = max(max_window, window)
        return max_window/k



        