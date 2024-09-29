class Solution(object):
    def maxOperations(self, nums, k):
        count = 0
        stack = {}
        for num in nums:
            comp = k - num
            if comp in stack and stack[comp] > 0:
                count += 1
                stack[comp] -= 1
            else:
                if num in stack:
                    stack[num] += 1
                else:
                    stack[num] = 1
        return count
            