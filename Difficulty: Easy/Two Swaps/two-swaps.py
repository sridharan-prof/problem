class Solution:
    def find_idx(self, arr, ele):
        # Find the index of the element 'ele' in the array 'arr'
        for i in range(len(arr)):
            if arr[i] == ele:
                return i
        return -1  # Return -1 if the element is not found (this shouldn't happen in this context)

    def checkSorted(self, arr):
        count = 0
        n = len(arr)

        for i in range(n):
            # Check if the current element is in the right place (i+1 for 1-based index)
            if arr[i] != i + 1:
                # Find the index of the correct element to swap with
                idx = self.find_idx(arr, i + 1)

                # Swap the elements
                arr[i], arr[idx] = arr[idx], arr[i]
                count += 1
                
                # If more than two swaps are made, return False
                if count > 2:
                    return False
        
        # Return True if no swaps were made (already sorted) or exactly two swaps were made
        return count == 0 or count == 2

    



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().split()))

        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")

# } Driver Code Ends