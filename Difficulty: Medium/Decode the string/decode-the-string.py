
class Solution:
    def decodedString(self, s):
        # code here
        stack = []
        
        for char in s:
            if char != "]":
                stack.append(char)
                
            else:
                substring = ""
                while stack and stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()
                
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                repeat_count = int(num)
                
                stack.append(substring * repeat_count)
        
        return "".join(stack) 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends