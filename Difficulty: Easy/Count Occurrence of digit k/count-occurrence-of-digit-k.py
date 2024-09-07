#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def num(self, k, arr):
        res = []
        count = 0
        for i in arr:
            for digit in str(i):
                if int(digit) == k:
                    count += 1
        return count

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.num(k,arr)
        print(res)
        t -= 1


# } Driver Code Ends