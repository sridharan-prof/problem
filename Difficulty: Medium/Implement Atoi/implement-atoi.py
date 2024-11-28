#User function template for Python
class Solution:
    def myAtoi(self, s):
        # Code here
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i < len(s) and s[i] == "+":
            set = 1
            i += 1
        elif i < len(s) and s[i] == "-":
            set = -1
            i += 1
        else:
            set = 1
        value = 0
        while i < len(s) and s[i].isnumeric():
            digit = ord(s[i]) - ord('0') 
            value = value * 10 + digit
            
            if set == 1 and value > 2147483647:
                return 2147483647
            if set == -1 and value > 2147483647:
                return -2147483648
            i += 1
        return set * value 

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends