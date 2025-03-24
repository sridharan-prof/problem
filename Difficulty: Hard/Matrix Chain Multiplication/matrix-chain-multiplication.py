class Solution:
    def matrixMultiplication(self, arr):
        # code here
        N = len(arr)
        dp = [[0] * N for _ in range(N)]

        for L in range(2, N):
            for i in range(1, N - L + 1):
                j = i + L - 1
                dp[i][j] = float('inf')

                for k in range(i, j):
                    cost = dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[1][N-1]  
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().matrixMultiplication(arr)  # find the missing number
    print(s)  # print the result
    print("~")

# } Driver Code Ends