#User function Template for python3
class Solution:
    def countWays(self, s):
        # code here
        memo = {}
        
        def solve(i, j, isTrue):
            if i > j:
                return 0
            if i == j:
                if isTrue:
                    return 1 if s[i] == 'T' else 0
                else:
                    return 1 if s[i] == 'F' else 0
            
            if (i, j, isTrue) in memo:
                return memo[(i, j, isTrue)]
            
            ways = 0
            for k in range(i + 1, j, 2):
                leftTrue = solve(i, k - 1, True)
                leftFalse = solve(i, k - 1, False)
                rightTrue = solve(k + 1, j, True)
                rightFalse = solve(k + 1, j, False)
                
                op = s[k]
                
                if op == '&':
                    if isTrue:
                        ways += leftTrue * rightTrue
                    else:
                        ways += leftFalse * rightTrue + leftTrue * rightFalse + leftFalse * rightFalse
                
                elif op == '|':
                    if isTrue:
                        ways += leftTrue * rightTrue + leftFalse * rightTrue + leftTrue * rightFalse
                    else:
                        ways += leftFalse * rightFalse
                
                elif op == '^':
                    if isTrue:
                        ways += leftTrue * rightFalse + leftFalse * rightTrue
                    else:
                        ways += leftTrue * rightTrue + leftFalse * rightFalse
            
            memo[(i, j, isTrue)] = ways
            return ways
        
        return solve(0, len(s) - 1, True)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        print(Solution().countWays(s))
        print("~")

# } Driver Code Ends