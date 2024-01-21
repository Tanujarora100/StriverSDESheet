from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        diagonal_sum = 0

        for i in range(n):
            diagonal_sum += mat[i][i]  # Add primary diagonal element

            if i != n - i - 1:  # Exclude the element common to both diagonals for odd-sized matrices
                diagonal_sum += mat[i][n - i - 1]  # Add secondary diagonal element

        return diagonal_sum