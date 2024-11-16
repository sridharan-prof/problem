#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	non_index = 0
    	
    	for num in range(len(arr)):
    	    if arr[num] != 0:
    	        arr[non_index] = arr[num]
    	        non_index += 1
    	for _ in range(non_index,len(arr)):
    	    arr[_] = 0
    	return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends