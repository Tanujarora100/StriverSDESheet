class Solution:
    def setZeroes(self, matrix):
        # Check if the matrix is empty
        if not matrix or not matrix[0]:
            return

        # Initialize arrays to keep track of rows and columns containing zeros
        row_array = [0] * len(matrix)  # Array to track zero rows
        col_array = [0] * len(matrix[0])  # Array to track zero columns
                                  
        # Find the rows and columns containing zeros
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_array[i] = 1  # Mark the row as containing zero
                    col_array[j] = 1  # Mark the column as containing zero

        # Set zeros in the corresponding rows and columns
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row_array[i] == 1 or col_array[j] == 1:
                    matrix[i][j] = 0  # Set the value to zero if the row or column contains a zero
