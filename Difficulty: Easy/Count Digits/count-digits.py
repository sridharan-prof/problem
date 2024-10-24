#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here
        string = str(N)
        num = list(string)
        count = 0
        for i in range(len(num)):
            number = int(num[i])
            if number == 0:
                pass
            elif N%number == 0:
                count += 1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
        print("~")
# } Driver Code Ends