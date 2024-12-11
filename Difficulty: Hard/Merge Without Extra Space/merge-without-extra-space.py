class Solution:
    def mergeArrays(self, a, b):
        # code here
        n=len(a)
        m=len(b)

        i=n-1
        j=0
        
        while i>=0 and j<m:
            if a[i]>b[j]:
                a[i],b[j]=b[j],a[i]
                
            else:
                break
            
            i-=1
            j+=1
        a.sort()
        b.sort()
        return a,b


#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

# } Driver Code Ends