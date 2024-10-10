class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        index_map = {}
        max_dist = 0
    
        for i in range(len(arr)):
            if arr[i] in index_map:
    
                dist = i - index_map[arr[i]]
                max_dist = max(max_dist, dist)
            else:
                index_map[arr[i]] = i
        
        return max_dist



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends