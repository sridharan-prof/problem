#User function Template for python3


class Solution:
    def minDiff(self,arr,k):
        arr.sort()
        min_diff = float("inf")
        
        for i in range(len(arr) - k + 1):
            curr_diff = arr[i + k - 1] - arr[i]
            min_diff = min(min_diff,curr_diff)
        return min_diff

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.minDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends