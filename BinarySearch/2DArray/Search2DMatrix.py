class Solution:
    def searchMatrix(self,matrix, target):
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        start, end = 0, rows * cols - 1

        while start <= end:
            mid = (start + end) // 2
            mid_element = matrix[mid // cols][mid % cols]

            if mid_element == target:
                return True
            elif mid_element < target:
                start = mid + 1
            else:
                end = mid - 1

        return False