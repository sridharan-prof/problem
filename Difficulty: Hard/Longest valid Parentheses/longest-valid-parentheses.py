
class Solution:
    def maxLength(self, s):
        # code here
        stack = [-1] 
        max_length = 0
    
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i) 
            else: 
                stack.pop() 
                if stack:
                    max_length = max(max_length, i - stack[-1])
                else:
                    stack.append(i) 
    
        return max_length

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))
        print("~")

# } Driver Code Ends