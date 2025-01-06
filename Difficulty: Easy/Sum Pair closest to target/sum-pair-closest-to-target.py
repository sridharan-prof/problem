#User function Template for python3
class Solution: 
    def sumClosest(self, arr, target):
        # code here
        arr.sort()
        n = len(arr)
    
        left, right = 0, n - 1
        closest_pair = []
        closest_diff = float('inf')
        max_abs_diff = -1
    
        while left < right:  # Ensure a != b (i.e., left != right)
            a, b = arr[left], arr[right]
            current_sum = a + b
            diff = abs(current_sum - target)
    
            # Update the closest pair based on diff and max absolute difference
            if diff < closest_diff or (diff == closest_diff and (b - a) > max_abs_diff):
                closest_diff = diff
                max_abs_diff = b - a
                closest_pair = [a, b]
    
            # Adjust pointers based on the current sum
            if current_sum < target:
                left += 1  # Increase sum
            elif current_sum > target:
                right -= 1  # Decrease sum
            else:  # Exact match
                break
    
        return closest_pair
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends