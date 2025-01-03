class Solution:
    def subarrayXor(self, arr, k):
        # code here
        xorCount = {}
        prefixXOR = 0
        count = 0
    
        for num in arr:
            prefixXOR ^= num
    
            # If current prefix XOR is equal to k
            if prefixXOR == k:
                count += 1
    
            # Check if there exists a prefixXOR such that prefixXOR ^ k = current prefixXOR
            requiredXOR = prefixXOR ^ k
            if requiredXOR in xorCount:
                count += xorCount[requiredXOR]
    
            # Update hash map with the current prefixXOR
            xorCount[prefixXOR] = xorCount.get(prefixXOR, 0) + 1
    
        return count


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends