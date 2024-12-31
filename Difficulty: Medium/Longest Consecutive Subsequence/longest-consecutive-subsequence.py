 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        if not arr:
            return 0

        # Step 1: Insert all elements into a HashSet
        elements_set = set(arr)
        longest_length = 0
    
        # Step 2: Traverse the array
        for num in arr:
            # Check if it's the start of a sequence
            if num - 1 not in elements_set:
                # Count the length of the consecutive sequence
                current_num = num
                current_length = 1
    
                while current_num + 1 in elements_set:
                    current_num += 1
                    current_length += 1
    
                # Update the longest length
                longest_length = max(longest_length, current_length)
    
        return longest_length

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().longestConsecutive(a))
        print("~")
# } Driver Code Ends