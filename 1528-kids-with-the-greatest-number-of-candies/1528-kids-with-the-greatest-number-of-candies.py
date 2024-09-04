class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ar = []
        add = 0
        gr = max(candies)
        for i in range(len(candies)):
            add = candies[i] + extraCandies
            if add >= gr:
                ar.append(True)
            else:
                ar.append(False)
        return ar

            
        