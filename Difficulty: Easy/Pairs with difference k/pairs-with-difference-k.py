from collections import defaultdict
class Solution:
    def countPairsWithDiffK(self,arr, k):
        res = 0
        mp = defaultdict(int)
        for n in arr:
            mp[n] += 1
        for n in arr:
            if mp[n+k] > 0:
                res += mp[n+k]
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends