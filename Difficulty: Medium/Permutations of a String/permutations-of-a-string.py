#User function Template for python3

class Solution:
    def findPermutation(self, s):
        # Code here
        def heap_permute(n, array):
            if n == 1:
                perm = "".join(array)
                if perm not in seen:  # Avoid adding duplicates
                    result.append(perm)
                    seen.add(perm)
                return
            for i in range(n):
                heap_permute(n - 1, array)
                # Swap based on the parity of n
                if n % 2 == 1:  # If n is odd
                    array[0], array[n - 1] = array[n - 1], array[0]
                else:  # If n is even
                    array[i], array[n - 1] = array[n - 1], array[i]

        result = []
        seen = set()  # Track unique permutations
        arr = list(s)
        heap_permute(len(arr), arr)
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends