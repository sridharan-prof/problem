class Solution:
    def maxValue(self, arr):
        lth=len(arr)
        dp=[0,0]+arr[1:]
        for ix in range(2,lth+1):
            dp[ix%3]=max(dp[(ix-1)%3],dp[(ix-2)%3]+arr[ix-1])
        mx=max(dp)
        dp=[0,0]+arr[:-1]
        for ix in range(2,lth+1):
            dp[ix%3]=max(dp[(ix-1)%3],dp[(ix-2)%3]+arr[ix-2])
        return max(mx,*dp)

#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = IntArray().Input()

        obj = Solution()
        res = obj.maxValue(arr)

        print(res)
        print("~")

# } Driver Code Ends