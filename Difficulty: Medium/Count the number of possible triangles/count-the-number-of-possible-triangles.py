#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        n = len(arr)
        arr.sort()  # Step 1: Sort the array
        count = 0
    
        # Step 2: Fix the largest side
        for k in range(n - 1, 1, -1):
            i = 0
            j = k - 1
            # Step 3: Use two pointers to find valid triangles
            while i < j:
                if arr[i] + arr[j] > arr[k]:
                    count += (j - i)  # All pairs (i, j-1), (i, j-2), ... are valid
                    j -= 1
                else:
                    i += 1
    
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends