#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        preffix_sum = 0
        count = 0
        preffix_sum_map = {0:1}
        
        for num in arr:
            preffix_sum += num
            
            if preffix_sum - tar in preffix_sum_map:
                count += preffix_sum_map[preffix_sum - tar]
            if preffix_sum in preffix_sum_map:
                preffix_sum_map[preffix_sum] += 1
            else:
                preffix_sum_map[preffix_sum] = 1
        return count
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends