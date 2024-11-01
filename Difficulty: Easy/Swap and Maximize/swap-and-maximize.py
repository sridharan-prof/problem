#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()

        # Create a new array to store the reordered elements
        reordered = []
        
        # Use two pointers to alternate between smallest and largest elements
        i, j = 0, len(arr) - 1
        while i <= j:
            if i == j:
                reordered.append(arr[i])
            else:
                reordered.append(arr[i])
                reordered.append(arr[j])
            i += 1
            j -= 1
    
        # Calculate the maximum sum of absolute differences
        max_sum = 0
        for k in range(len(reordered)):
            max_sum += abs(reordered[k] - reordered[(k + 1) % len(reordered)])
    
        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends