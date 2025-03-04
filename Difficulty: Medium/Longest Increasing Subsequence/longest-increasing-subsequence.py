from bisect import bisect_left
from typing import List

class Solution:
    def lis(self, arr):
        # code here
        if not arr:
            return 0
        
        dp = []
        
        for num in arr:
            pos = bisect_left(dp, num)
            
            if pos == len(dp):
                dp.append(num)
            else:
                dp[pos] = num
        
        return len(dp)


#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    for _ in range(int(input())):
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.lis(a))
        print("~")
# } Driver Code Ends