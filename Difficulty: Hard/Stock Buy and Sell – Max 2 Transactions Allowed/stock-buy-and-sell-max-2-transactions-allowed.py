class Solution:
    def maxProfit(self, prices):
        # code here
        if not prices:
            return 0
    
        first_buy = float('inf')
        first_sell = 0
        second_buy = float('inf')
        second_sell = 0
    
        for price in prices:
            first_buy = min(first_buy, price) 
            first_sell = max(first_sell, price - first_buy)
            second_buy = min(second_buy, price - first_sell)
            second_sell = max(second_sell, price - second_buy)
            
        return second_sell

#{ 
 # Driver Code Starts
#Initial template for Python 3
import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxProfit(arr))
        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends