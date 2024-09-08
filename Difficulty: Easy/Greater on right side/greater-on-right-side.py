#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:

	def nextGreatest(self,arr):
	    n = len(arr)
	    res = [-1] * n
	    maxi = -1
		for i in range(n-1,-1,-1):
		    res[i] = maxi
		    maxi = max(maxi,arr[i])
	    
	    return res
#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.nextGreatest(arr)
        print(*ans)
        t -= 1


# } Driver Code Ends