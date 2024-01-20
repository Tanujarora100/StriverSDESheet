from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        start = 1
        limit = n * n
        row_start = 0
        row_end = n - 1
        col_start = 0
        col_end = n - 1
        
        while start <= limit:
            # Fill the topmost row
            for j in range(col_start, col_end + 1):
                matrix[row_start][j] = start
                start += 1
            row_start += 1
            
            # Fill the rightmost column
            for i in range(row_start, row_end + 1):
                matrix[i][col_end] = start
                start += 1
            col_end -= 1
            
            # Fill the bottommost row
            if row_start <= row_end:
                for j in range(col_end, col_start - 1, -1):
                    matrix[row_end][j] = start
                    start += 1
                row_end -= 1
            
            # Fill the leftmost column
            if col_start <= col_end:
                for i in range(row_end, row_start - 1, -1):
                    matrix[i][col_start] = start
                    start += 1
                col_start += 1
        
        return matrix