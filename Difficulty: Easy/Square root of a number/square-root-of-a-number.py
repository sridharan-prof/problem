#Complete this function
class Solution:
    def floorSqrt(self, n): 
        sqrt = n**0.5
        decimal_value = int(sqrt)
        return decimal_value
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        x = int(input())

        print(Solution().floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends