from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #Get the transpose of the matrix
        #Reverse every row

        ROWS= len(matrix)
        COLS= len(matrix[0])
        for i in range(ROWS):
            for j in range(i,COLS):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #Swap across the main diagonal of the matrix
        for i in range(ROWS):
            left=0
            right= COLS-1
            #Reverse every row of the matrix.
            while left <right:
                matrix[i][left],matrix[i][right]=matrix[i][right],matrix[i][left]
                left+=1
                right-=1
        return matrix
        