#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution: 
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        arr.sort()  # Sorting the array
        left, right = 0, len(arr) - 1
        count = 0
    
        while left < right:
            # Check the sum of the current pair
            if arr[left] + arr[right] < target:
                # All pairs with `left` and any element between `left+1` and `right` are valid
                count += (right - left)
                left += 1  # Move left pointer forward
            else:
                right -= 1  # Move right pointer backward
        
        return count

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends