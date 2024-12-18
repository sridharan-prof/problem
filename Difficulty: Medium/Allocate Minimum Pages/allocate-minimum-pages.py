class Solution:
    
    def check(self, arr, k, mid):
        number, pages = 1, 0
        for i in range(len(arr)):
            if arr[i] > mid:
                return False
            if pages + arr[i] > mid:
                pages = arr[i]
                number += 1
            else:
                pages += arr[i]
        return number <= k

    def findPages(self, arr, k):
        if len(arr) < k:
            return -1
        lo, hi = 0, sum(arr)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.check(arr, k, mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends