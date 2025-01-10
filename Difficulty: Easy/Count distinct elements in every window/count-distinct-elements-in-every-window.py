
class Solution:
    def countDistinct(self, arr, k):
        result = []
        freq_map = {}
    
        for i in range(k):
            freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1
            
        result.append(len(freq_map))
    
        for i in range(k, len(arr)):
            if freq_map[arr[i - k]] == 1:
                del freq_map[arr[i - k]]
            else:
                freq_map[arr[i - k]] -= 1
                
            freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1
    
            result.append(len(freq_map))
    
        return result


#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends