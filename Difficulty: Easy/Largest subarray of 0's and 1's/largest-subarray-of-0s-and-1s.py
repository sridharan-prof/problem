class Solution:
    def maxLen(self, arr):
        # code here
        arr = [-1 if num == 0 else 1 for num in arr]

        sum_index_map = {0: -1}
        max_length = 0
        running_sum = 0
    
        for i, num in enumerate(arr):
            running_sum += num
            if running_sum in sum_index_map:
                max_length = max(max_length, i - sum_index_map[running_sum])
            else:
                sum_index_map[running_sum] = i
    
        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends