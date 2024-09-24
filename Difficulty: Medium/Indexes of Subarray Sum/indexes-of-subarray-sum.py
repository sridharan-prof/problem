#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        if s == 0:
            for i in range(n):
                if arr[i] == 0:
                    return [i + 1, i + 1]
            return [-1]
            
        start = 0
        curr_sum = 0
        
        for i in range(n):
            curr_sum += arr[i]
            
            while curr_sum > s and start <= i:
                curr_sum -= arr[start]
                start += 1
            if curr_sum == s:
                return [start + 1, i + 1]
            
        return [-1]

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends