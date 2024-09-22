#User function Template for python3

class Solution:
    def Selection(self, arr):
        
        mod = 10**9 + 7
        arr.sort()
        
        x = 0
        res = 0
        for i in arr:
            res += (i * x)
            res %= mod
            x += 1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.Selection(arr)
        print(res)
        t -= 1
# } Driver Code Ends