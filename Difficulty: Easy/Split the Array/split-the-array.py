#User function Template for python3
class Solution:
    
	def countgroup(self,arr): 
        MOD = 10**9 + 7
        
        # Calculate XOR of all elements
        xor_sum = 0
        for num in arr:
            xor_sum ^= num
        
        # If XOR is not 0, no valid split exists
        if xor_sum != 0:
            return 0
        
        # If XOR is 0, count the number of ways to choose a subset
        n = len(arr)
        return (pow(2, n-1, MOD) - 1) % MOD
		    
		    


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countgroup(arr)
        print(res)
        t -= 1

# } Driver Code Ends