class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            total = n1 + n2 + carry
            carry = total // 10
            result.append(str(total % 10))

            i -= 1
            j -= 1

        # Join and strip leading zeros from the result
        return ''.join(result[::-1]).lstrip('0') or '0'

    def minSum(self, arr):
        n = len(arr)
        arr.sort()

        ans1 = ans2 = ''

        # Distribute digits alternately between ans1 and ans2
        for i in range(n):
            if i%2==0:
                ans1+=str(arr[i])
            else:
                ans2+=str(arr[i])

        # Use the custom addStrings function to return the sum as a string
        return self.addStrings(ans1, ans2)





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSum(arr)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends