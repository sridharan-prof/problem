from collections import deque

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])

        def bfs(grid, i, j):
            # Directions for 8 neighboring cells (up, down, left, right, and 4 diagonals)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            
            # Use deque for efficient queue management
            queue = deque([(i, j)])
            
            # Mark the starting cell as visited by setting it to 0
            grid[i][j] = 0
            
            while queue:
                x, y = queue.popleft()
                
                # Explore all 8 possible directions
                for d in directions:
                    new_x, new_y = x + d[0], y + d[1]
                    
                    # Ensure the new coordinates are within bounds and still land (1)
                    if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 1:
                        queue.append((new_x, new_y))
                        grid[new_x][new_y] = 0  # Mark this cell as visited

        island_count = 0

        # Iterate through the grid and start BFS from every unvisited land cell (1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:  # If we find an unvisited land cell
                    bfs(grid, i, j)   # Perform BFS to visit the entire island
                    island_count += 1 # Increment the island count
        
        return island_count


#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.numIslands(grid))

# } Driver Code Ends