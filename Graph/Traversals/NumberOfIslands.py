from typing import List
from collections import deque

class NumberOfIslands:
    def isValid(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1'

    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(i, j, grid, directions)
                    islands += 1

        return islands

    def bfs(self, i, j, grid, directions):
        q = deque([(i, j)])

        while q:
            x, y = q.popleft()

            for dir in directions:
                nx, ny = x + dir[0], y + dir[1]

                if self.isValid(nx, ny, grid):
                    q.append((nx, ny))
                    grid[nx][ny] = '0'

# Example usage:
grid = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]

solution = NumberOfIslands()
result = solution.numIslands(grid)
print(result)
