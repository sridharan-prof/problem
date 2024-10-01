class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res = []
        for i in range(len(gain)):
            if i != 0:
                gain[i] += gain[i-1]
            if gain[i] > 0:
                res.append(gain[i])
        
        return max(res) if res else 0