class Solution(object):
    def increasingTriplet(self, nums):
        fst = sec = float("inf")

        for num in nums:
            if num <= fst:
                fst = num
            elif num <= sec:
                sec = num
            else:
                return True
        return False

        