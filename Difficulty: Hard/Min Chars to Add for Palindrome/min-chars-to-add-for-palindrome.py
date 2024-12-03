class Solution:
    def minChar(self, pattern):

        combined = s + '#' + s[::-1]
        lps = [0] * len(combined)
        
        for i in range(1, len(combined)):
            length = lps[i - 1]
            while length > 0 and combined[i] != combined[length]:
                length = lps[length - 1]
            if combined[i] == combined[length]:
                length += 1
            lps[i] = length
        
        return len(s) - lps[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends