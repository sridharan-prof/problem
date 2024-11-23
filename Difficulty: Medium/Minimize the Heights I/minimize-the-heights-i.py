#User function Template for python3

class Solution:
    def getMinDiff(self,k, arr):
        # code here
        arr.sort()
        n = len(arr)
        
        # Initialize the answer with the current max difference
        ans = arr[-1] - arr[0]
        
        # Traverse the array and calculate the possible minimum differences
        for i in range(1, n):
            # Calculate the minimum and maximum heights after modification
            min_height = min(arr[0] + k, arr[i] - k)
            max_height = max(arr[i - 1] + k, arr[-1] - k)
            
            # Update the answer with the smallest difference
            ans = min(ans, max_height - min_height)
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.getMinDiff(k, arr)
        print(res)
        print("~")

# } Driver Code Ends