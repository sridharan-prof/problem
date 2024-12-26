#User function Template for python3
class Solution:
	def twoSum(self, arr, target):
		# code here
		num_map = {}
		for i,num in enumerate(arr):
            comp = target - num
            if comp in num_map:
                return [num_map[comp],i]
            num_map[num] = i
        return []

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.twoSum(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends