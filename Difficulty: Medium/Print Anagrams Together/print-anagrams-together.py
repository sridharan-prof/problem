#User function Template for python3
from collections import defaultdict

class Solution:

    def anagrams(self, arr):
        
        anagrams = defaultdict(list)
        for string in arr:
            sorted_string = ''.join(sorted(string))
            anagrams[sorted_string].append(string)
        
        # Create the result by extracting groups in order of their appearance
        result = list(anagrams.values())
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends