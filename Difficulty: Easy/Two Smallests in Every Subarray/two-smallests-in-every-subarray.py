class Solution:
    def pairWithMaxSum(self, arr):
        n = len(arr)
        if len(arr) < 2:
            return -1
        
        max_sum = -1
        
        for i in range(n-1):
            smallest = min(arr[i], arr[i+1])
            second_smallest = max(arr[i], arr[i+1])
            
            cur_sum = smallest + second_smallest
            
            max_sum = max(max_sum, cur_sum)
        return max_sum


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    t = int(data[0])
    lines = data[1:]

    for line in lines:
        s = list(map(int, line.strip().split()))
        solution = Solution()
        res = solution.pairWithMaxSum(s)
        print(res)

# } Driver Code Ends