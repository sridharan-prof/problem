#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		max_ending = arr[0]
		min_ending = arr[0]
		max_product = arr[0]
		if not arr:
		    return 0
		
		for cur in arr[1:]:
		    if cur < 0:
		        max_ending, min_ending = min_ending, max_ending
		 
		    max_ending = max(cur, cur*max_ending)
		    min_ending = min(cur, cur*min_ending)
		    
		    max_product = max(max_product, max_ending)
		    
	    return max_product
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends