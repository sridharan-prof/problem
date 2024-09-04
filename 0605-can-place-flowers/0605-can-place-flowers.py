class Solution(object):
    def canPlaceFlowers(self, arr, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        x = 0
        for i in range(len(arr)):
            if (i == 0 or arr[i-1] == 0) and (i == len(arr)-1 or arr[i+1] == 0) and arr[i] == 0:
                arr[i] = 1
                x += 1
        return n <= x
        