#User function Template for python3
class Solution:
	def minJumps(self, nums):
	    # code here
        if len(nums) <= 1:
            return 0
        if nums[0] == 0:
            return -1

        jumps = 0
        cur_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == cur_end:
                jumps += 1
                cur_end = farthest
            if cur_end >= len(nums)-1:
                break
        return jumps if  cur_end >= len(nums)-1 else -1
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends