class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        result = []
        if not mat or not mat[0]:
            return result
        
        top, bottom = 0, len(mat) - 1
        left, right = 0, len(mat[0]) - 1
        
        while top <= bottom and left <= right:
            # Traverse from left to right
            for col in range(left, right + 1):
                result.append(mat[top][col])
            top += 1
            
            # Traverse from top to bottom
            for row in range(top, bottom + 1):
                result.append(mat[row][right])
            right -= 1
            
            if top <= bottom:
                # Traverse from right to left
                for col in range(right, left - 1, -1):
                    result.append(mat[bottom][col])
                bottom -= 1
            
            if left <= right:
                # Traverse from bottom to top
                for row in range(bottom, top - 1, -1):
                    result.append(mat[row][left])
                left += 1
        
        return result


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends