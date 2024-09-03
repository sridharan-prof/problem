#User function Template for python3

class Solution:
    def customSort(self, arr):
        n = len(arr)//2
        a = sorted(arr[0:n])
        b = sorted(arr[n:], reverse = True)
        return a + b
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.customSort(arr)
        print(*ans)
        # print("~")
        t -= 1

# } Driver Code Ends