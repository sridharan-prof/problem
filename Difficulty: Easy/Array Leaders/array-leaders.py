class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self,n, arr):
        if not arr:
            return []
        lst=[]
        maximum=arr[-1]
        lst.append(maximum)
        
        for i in range(n-2,-1,-1):
            if arr[i] >= maximum:
                lst.append(arr[i])
                maximum = arr[i]
        lst.reverse()
        return lst
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        obj = Solution()

        A = obj.leaders(N, A)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends