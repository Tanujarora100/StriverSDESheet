class Solution:
    def searchMatrix(self, matrix, target):
        # Check if the matrix is empty
        if not matrix or not matrix[0]:
            return False

        # Get the number of rows and columns in the matrix
        rows, cols = len(matrix), len(matrix[0])
        # Start from the top-right corner of the matrix
        r, c = 0, cols - 1

        # Loop until we reach the bottom-left corner of the matrix
        while r < rows and c >= 0:
            # If the current element is equal to the target, return True
            if matrix[r][c] == target:
                return True
            # If the current element is greater than the target, move left in the matrix
            elif matrix[r][c] > target:
                c -= 1
            # If the current element is less than the target, move down in the matrix
            elif matrix[r][c] < target:
                r += 1

        # If the target is not found, return False
        return False

