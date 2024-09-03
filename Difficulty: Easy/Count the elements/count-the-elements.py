#User function Template for python3
class Solution:
    def countElements(self, a, b, n, query, q):
        max_val = max(max(a), max(b))
        freq = [0] * (max_val + 1)
        for elem in b:
            freq[elem] += 1

        cf = [0] * (max_val + 1)
        cf[0] = freq[0]

        for i in range(1, max_val + 1):
            cf[i] = cf[i - 1] + freq[i]

        result = []
        for x in query:
            result.append(cf[a[x]])
        
        return result
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends