#User function Template for python3
class Solution:
	def addBinary(self, a, b):
		# code here
	    max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        result = []
        carry = 0

        for i in range(max_len - 1, -1, -1):
            digit_sum = int(a[i]) + int(b[i]) + carry
            carry = digit_sum // 2
            result.append(str(digit_sum % 2)) 
            
        if carry:
            result.append('1')

        binary_list = ''.join(result[::-1])
        return binary_list.lstrip('0') or '0'
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends