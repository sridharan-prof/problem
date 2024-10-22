#User function Template for python3


class Solution:
    def sameOccurrence(self, arr, x, y):
        # code here
        preffix_count = {0:1}
        diff = 0
        count = 0
        for num in arr:
            if num == x:
                diff += 1
            if num == y:
                diff -= 1
            if diff in preffix_count:
                count += preffix_count[diff]
            if diff in preffix_count:
                preffix_count[diff] += 1
            else:
                preffix_count[diff] = 1
        
        return count
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        y = int(input().strip())
        ob = Solution()
        ans = ob.sameOccurrence(arr, x, y)
        print(ans)
        tc -= 1

# } Driver Code Ends