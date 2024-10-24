#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        for i in range(len(arr)-1):
            if arr[i] != 0 and arr[i+1] != 0 and arr[i] == arr[i+1]:
                arr[i] = arr[i]*2
                arr[i+1] = 0
                
        self.zeros(arr)
        return arr
    def zeros(self, arr):
        k = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[k] = arr[i]
                k += 1
        for j in range(k, len(arr)):
            arr[j] = 0


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        t -= 1


# } Driver Code Ends