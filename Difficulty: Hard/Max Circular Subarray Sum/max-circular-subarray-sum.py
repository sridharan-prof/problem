#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    totalsum = 0
    curmaxsum = 0
    curminsum = 0
    maxsum = arr[0]
    minsum = arr[0]
    
    for i in arr:
        
        curmaxsum = max(i, curmaxsum+i)
        maxsum = max(maxsum, curmaxsum)
        
        curminsum = min(i,curminsum+i)
        minsum = min(curminsum, minsum)
        
        totalsum += i
        
    normalsum = maxsum
    circularsum = totalsum - minsum
    
    if totalsum == minsum:
        return normalsum
    return max(circularsum, normalsum)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends