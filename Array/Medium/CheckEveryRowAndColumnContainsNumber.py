from collections import defaultdict


class Solution:
    def checkValid(self, matrix):
        m, n = len(matrix), len(matrix[0])

        rows, cols = defaultdict(set), defaultdict(set)

        for i in range(m):
            for j in range(n):
                if (matrix[i][j] in rows[i]) or (matrix[i][j] in cols[j]):
                    return False
                else:
                    rows[i].add(matrix[i][j])
                    cols[j].add(matrix[i][j])

        return True
