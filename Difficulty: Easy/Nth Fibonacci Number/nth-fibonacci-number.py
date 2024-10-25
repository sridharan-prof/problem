class Solution:
    def nthFibonacci(self, n : int) -> int:
        if n == 1 or n == 2:
            return 1
        else:
            a, b = 1, 1
            for i in range(3, n+1):
                a, b = b, (a+b) % 1000000007
            return b 
#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

        print("~")
# } Driver Code Ends