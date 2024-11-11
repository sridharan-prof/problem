#User function Template for python3

class Solution:
    def minIncrements(self, arr): 
        # Code here
        arr.sort()
        
        # Initialize the count of increments
        increments = 0
        
        # Loop through the array, starting from the second element
        for i in range(1, len(arr)):
            # If the current element is not greater than the previous, increment it
            if arr[i] <= arr[i - 1]:
                # Calculate the increment needed
                increment_needed = arr[i - 1] + 1 - arr[i]
                
                # Add to the count of increments
                increments += increment_needed
                
                # Update the current element to be unique
                arr[i] = arr[i - 1] + 1
        
        return increments


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr))

        T -= 1

# } Driver Code Ends