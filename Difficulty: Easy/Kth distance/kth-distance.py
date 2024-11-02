#User function Template for python3
from collections import Counter
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        if k <= 0:
            return False
        
        count = Counter()
        
        # Initialize the first window of size k
        for i in range(min(k+1, len(arr))):
            count[arr[i]] += 1
            if count[arr[i]] > 1:
                return True
        
        # Slide the window across the array
        for i in range(k+1, len(arr)):
            # Remove the element that is sliding out of the window
            count[arr[i - (k+1)]] -= 1
            if count[arr[i - (k+1)]] == 0:
                del count[arr[i - (k+1)]]
            
            # Add the new element
            count[arr[i]] += 1
            if count[arr[i]] > 1:
                return True
        
        return False


#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.checkDuplicatesWithinK(arr, k)
        if res:
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1
# } Driver Code Ends