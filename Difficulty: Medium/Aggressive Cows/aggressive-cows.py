#User function Template for python3
class Solution:
    def check(self,stalls,k,dis):
        c = 1
        pre = stalls[0]
        for i in range(1,len(stalls)):
            if stalls[i] - pre >= dis:
                pre = stalls[i]
                c += 1
        return c >= k

    def aggressiveCows(self, stalls, k):
        stalls.sort()
        ans = 0
        low = 1
        high = stalls[-1] - stalls[0]
        while low <= high:
            mid = low +(high - low) // 2
            if self.check(stalls,k,mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
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
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends