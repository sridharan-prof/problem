#User function Template for python3

class Solution:
    def MaxWeightDiff(self, arr,k):
        arr.sort()
        
        total = sum(arr)
        
        smallest_sum = sum(arr[:k])
        
        largest_sum = sum(arr[-k:])
        
        smallest_result = abs(smallest_sum - (total - smallest_sum))
        greatest_result = abs(largest_sum - (total - largest_sum))
        
        return max(smallest_result, greatest_result)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.MaxWeightDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends