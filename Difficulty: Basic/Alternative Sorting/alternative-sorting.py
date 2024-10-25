class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        left = 0
        right = len(arr) - 1
        arr.sort()
        res = []        
        while left <= right:
            if right >= left:
                res.append(arr[right])
                right -= 1
            if left <= right:
                res.append(arr[left])
                left += 1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends