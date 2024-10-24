# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,str):
        # code here
        word = str.split(".")
        splt_word = word[::-1]
        res = ".".join(splt_word)
        return res

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

        print("~")
# } Driver Code Ends