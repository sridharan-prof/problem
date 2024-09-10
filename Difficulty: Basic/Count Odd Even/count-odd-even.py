#User function Template for python3

class Solution:
	def countOddEven(self, arr):
		odd = 0
		even = 0
		for i in range(len(arr)):
		    if arr[i]%2 == 0:
		        even += 1
		    else:
		        odd += 1
	    return odd,even


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    # Testcase input
    testcase = int(input())

    for _ in range(testcase):

        arr = list(map(int, input().split()))

        # Creating an object of the Solution class
        ob = Solution()

        # Calling the function to count even and odd
        res = ob.countOddEven(arr)

        # Printing the result
        print(*res)

# } Driver Code Ends