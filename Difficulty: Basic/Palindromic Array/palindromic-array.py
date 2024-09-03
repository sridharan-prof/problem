# Your task is to complete this function
# Function should return true/false
def PalinArray(arr):
    for num in arr:
        st = str(num)
        if st != st[::-1]:
            return False
    return True


#{ 
 # Driver Code Starts
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr):
            print("true")
        else:
            print("false")
# Contributed By: Harshit Sidhwa

# } Driver Code Ends