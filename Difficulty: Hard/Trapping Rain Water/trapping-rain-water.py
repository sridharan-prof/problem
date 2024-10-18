
class Solution:
    def trappingWater(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        left_max = [0]*n
        right_max = [0]*n
        
        left_max[0] = arr[0]
        for i in range(1,n):
            left_max[i] = max(left_max[i-1],arr[i])
        
        right_max[n-1] = arr[n-1]
        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1],arr[i])
            
        trapped_water = 0
        for i in range(n):
            trapped_water += min(left_max[i],right_max[i])-arr[i]
        return trapped_water

#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.trappingWater(arr))

        t -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends