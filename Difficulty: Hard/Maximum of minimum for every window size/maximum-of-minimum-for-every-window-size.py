
class Solution:
    def maxOfMins(self, arr):
       # code here
        n = len(arr)
        
        next_smaller = [n] * n
        prev_smaller = [-1] * n
        
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                next_smaller[stack.pop()] = i
            stack.append(i)
        
        stack = []
        
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                prev_smaller[stack.pop()] = i
            stack.append(i)
        
        window_size = [0] * n
        for i in range(n):
            length = next_smaller[i] - prev_smaller[i] - 1
            window_size[length-1] = max(window_size[length-1], arr[i])
        
        for i in range(n-2, -1, -1):
            window_size[i] = max(window_size[i], window_size[i+1])
        
        return window_size

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        solution = Solution()
        result = solution.maxOfMins(arr)
        print(" ".join(map(str, result)))
        print("~")
# } Driver Code Ends