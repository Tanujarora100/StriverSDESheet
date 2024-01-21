from collections import deque

class Solution:


    def shortestBridge(self, grid):
        n = len(grid)  # Get the size of the grid
        queue = deque()  # Initialize a queue for BFS

        # Find the first island using DFS
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, n, i, j, queue)
                    found = True
                    break
            if found:
                break

        # Perform BFS to find the shortest bridge to the second island
        distance = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Define the four directions to move
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                for dirs in directions:
                    x, y = cur[0] + dirs[0], cur[1] + dirs[1]
                    if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] == 2:
                        continue
                    if grid[x][y] == 1:  # Found the second island
                        return distance
                    queue.append([x, y])
                    grid[x][y] = 2  # Mark as visited
            distance += 1
        return -1  # If no bridge is found, return -1

    def dfs(self, grid, n, i, j, queue):
        if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] == 0 or grid[i][j] == 2:
            return

        queue.append([i, j])
        grid[i][j] = 2
        self.dfs(grid, n, i + 1, j, queue)
        self.dfs(grid, n, i, j + 1, queue)
        self.dfs(grid, n, i - 1, j, queue)
        self.dfs(grid, n, i, j - 1, queue)
