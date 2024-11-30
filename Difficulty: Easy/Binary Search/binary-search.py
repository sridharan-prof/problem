#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        if k not in arr:
            return -1
        return arr.index(k)
            



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)
        print("~")

# } Driver Code Ends