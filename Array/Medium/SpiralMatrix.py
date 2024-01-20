from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0:
            return res
        row_begin = 0
        col_begin = 0
        row_end = len(matrix) - 1
        col_end = len(matrix[0]) - 1
        total_items = len(matrix) * len(matrix[0])
        curr_items = 0

        while row_begin <= row_end and col_begin <= col_end and curr_items< total_items:
            # Print the top row
            for i in range(col_begin, col_end + 1):
                res.append(matrix[row_begin][i])
                curr_items += 1
                if curr_items >= total_items:
                    break
            row_begin += 1

            # Print the rightmost column
            for i in range(row_begin, row_end + 1):
                res.append(matrix[i][col_end])
                curr_items += 1
                if curr_items >= total_items:
                    break
            col_end -= 1

            # Print the bottom row
            if row_begin <= row_end:
                for i in range(col_end, col_begin - 1, -1):
                    res.append(matrix[row_end][i])
                    curr_items += 1
                    if curr_items >= total_items:
                        break
                row_end -= 1

            # Print the leftmost column
            if col_begin <= col_end:
                for i in range(row_end, row_begin - 1, -1):
                    res.append(matrix[i][col_begin])
                    curr_items += 1
                    if curr_items >= total_items:
                        break
                col_begin += 1

        return res
