from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, arr, x):
        if not arr:
            return []
        
        n = len(arr)
        l, max_len, start_idx = 0, 0, 0
        max_deque, min_deque = deque(), deque()

        for r in range(n):
            # Maintain max_deque (always decreasing)
            while max_deque and arr[max_deque[-1]] < arr[r]:
                max_deque.pop()
            max_deque.append(r)

            # Maintain min_deque (always increasing)
            while min_deque and arr[min_deque[-1]] > arr[r]:
                min_deque.pop()
            min_deque.append(r)

            # Shrink window if difference exceeds x
            while arr[max_deque[0]] - arr[min_deque[0]] > x:
                l += 1
                # Remove elements that are out of the window
                if max_deque[0] < l:
                    max_deque.popleft()
                if min_deque[0] < l:
                    min_deque.popleft()

            # Update longest subarray
            if r - l + 1 > max_len:
                max_len = r - l + 1
                start_idx = l  # Store the start index
        
        return arr[start_idx:start_idx + max_len]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.longestSubarray(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends