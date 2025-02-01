class Solution:
	def isWordExist(self, mat, word):
		#Code here
        if not mat or not mat[0]:
            return False
    
        n, m = len(mat), len(mat[0])
    
        def dfs(x, y, index):
            if index == len(word):  # Found the word
                return True
            
            if x < 0 or x >= n or y < 0 or y >= m or mat[x][y] != word[index]:
                return False
            
            # Temporarily mark the cell as visited
            temp = mat[x][y]
            mat[x][y] = '#'  
    
            # Explore all four directions
            found = (dfs(x + 1, y, index + 1) or
                     dfs(x - 1, y, index + 1) or
                     dfs(x, y + 1, index + 1) or
                     dfs(x, y - 1, index + 1))
    
            # Restore the cell
            mat[x][y] = temp  
    
            return found
    
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0] and dfs(i, j, 0):
                    return True
    
        return False

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            mat.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(mat, word)
        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends