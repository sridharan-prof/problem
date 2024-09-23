#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def sortedMerge(self, arr1,arr2,res):
        arr1.extend(arr2)
        res[:] = sorted(arr1)
        
        
        # Your code goes here

#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        # First line contains the sizes of the arrays
        # Split the combined list into arr1 and arr2
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))

        n = len(arr1)
        m = len(arr2)

        res = [0] * (n + m)  # Initialize the result array with size n + m
        ob = Solution()
        ob.sortedMerge(arr1, arr2, res)

        # Print the merged array
        for i in res:
            print(i, end=" ")
        print()
# } Driver Code Ends