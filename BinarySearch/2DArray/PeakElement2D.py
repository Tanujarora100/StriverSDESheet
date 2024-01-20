class Solution:
    def findRow(self, mat, col, m, n):
        maxi = -1
        index = -1
        for i in range(n):
            if mat[i][col] > maxi:
                maxi = mat[i][col]
                index = i
        return index

    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])
        low, high = 0, m - 1

        while low <= high:
            midcol = low + (high - low) // 2
            midrow = self.findRow(mat, midcol, m, n)
            left = mat[midrow][midcol - 1] if midcol - 1 >= low else -1
            right = mat[midrow][midcol + 1] if midcol < high else -1

            if mat[midrow][midcol] > left and mat[midrow][midcol] > right:
                return [midrow, midcol]
            elif mat[midrow][midcol] < left:
                high = midcol - 1
            else:
                low = midcol + 1

        return [-1, -1]


#
