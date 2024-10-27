class Solution:
    def findTriplet(self, arr):
        n = len(arr)
        
        for i in range(n):
            seen = set()
            
            for j in range(n):
                if i != j:
                    if arr[i] - arr[j] in seen:
                        return True
                    seen.add(arr[j])
        return False
#{ 
 # Driver Code Starts
#Initial Template for Python 3
# Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findTriplet(arr)
        if (res):
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1

# } Driver Code Ends