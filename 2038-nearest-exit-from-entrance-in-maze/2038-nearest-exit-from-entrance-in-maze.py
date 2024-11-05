class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row, col = len(maze),len(maze[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[False]*col for _ in range(row)]
        visited[entrance[0]][entrance[1]] = True
        que = deque([(*entrance,0)])

        while len(que) > 0:

            i,j,depth = que.popleft()
            if (i in {0, row-1} or j in {0, col-1}) and [i,j] != entrance:
                return depth

            for x,y in directions:
                x = x+i
                y = y+j

                if 0 <= x < row and 0 <= y < col and not visited[x][y] and maze[x][y] == ".":
                    que.append((x,y,depth + 1))
                    visited[x][y] = True
        return -1
