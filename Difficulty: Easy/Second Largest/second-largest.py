#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
           return -1
        else:
            first = sec = float('-inf')
            for num in arr:
                if num > first:
                    sec = first
                    first = num
                elif num > sec and num != first:
                    sec = num
            return sec if sec != float('-inf') else -1


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)

# } Driver Code Ends