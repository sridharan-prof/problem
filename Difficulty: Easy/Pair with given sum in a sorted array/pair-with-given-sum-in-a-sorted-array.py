#User function Template for python3


class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        left, right = 0, len(arr) - 1
        count = 0
    
        while left < right:
            current_sum = arr[left] + arr[right]
    
            if current_sum == target:
                if arr[left] == arr[right]:
                    # When both pointers point to the same value
                    n = right - left + 1
                    count += (n * (n - 1)) // 2  # Count all pairs (combinations)
                    break  # No need to continue, as we've counted all pairs
                else:
                    # Count duplicates for arr[left]
                    left_count, right_count = 1, 1
    
                    # Count consecutive duplicates on the left
                    while left + 1 < right and arr[left] == arr[left + 1]:
                        left_count += 1
                        left += 1
    
                    # Count consecutive duplicates on the right
                    while right - 1 > left and arr[right] == arr[right - 1]:
                        right_count += 1
                        right -= 1
    
                    # Total pairs = left_count * right_count
                    count += left_count * right_count
    
                    # Move both pointers
                    left += 1
                    right -= 1
    
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
        return count
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends