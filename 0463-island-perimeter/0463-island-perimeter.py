class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        peri = 0
        rows, col = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(col):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0:
                        peri += 1
                    if i == rows - 1 or grid[i+1][j] == 0:
                        peri += 1
                    if j == 0 or grid[i][j-1] == 0:
                        peri += 1
                    if j == col - 1 or grid[i][j+1] == 0:
                        peri += 1
        return peri 