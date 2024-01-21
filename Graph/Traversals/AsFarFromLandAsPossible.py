from collections import deque

class FarClass:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class Solution:
    def maxDistance(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        pq = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    pq.append(FarClass(i, j))

        if len(pq) == -1 or len(pq) == ROWS * COLS:
            return -1

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        loop_count = 0

        while pq:
            size = len(pq)
            loop_count += 1

            for _ in range(size):
                curr_cell = pq.popleft()
                row, col = curr_cell.row, curr_cell.col

                for dr, dc in dirs:
                    new_row, new_col = row + dr, col + dc

                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == 0:
                        pq.append(FarClass(new_row, new_col))
                        grid[new_row][new_col] = 1

        return loop_count - 1
