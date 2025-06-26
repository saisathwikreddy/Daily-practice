# Last updated: 6/26/2025, 2:34:55 PM
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        isFirstRowZero, isFirstColZero = False, False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                isFirstColZero = True
                break
        
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                isFirstRowZero = True
                break

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if isFirstColZero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
        if isFirstRowZero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        