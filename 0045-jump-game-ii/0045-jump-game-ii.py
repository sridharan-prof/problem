class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        if nums[0] == 0:
            return -1

        jumps = 0
        cur_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == cur_end:
                jumps += 1
                cur_end = farthest
            if cur_end >= len(nums)-1:
                break
        return jumps if  cur_end >= len(nums)-1 else -1
        