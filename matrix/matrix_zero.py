from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Determine the size of the matrix
        m, n = len(matrix), len(matrix[0])
        
        # Variables to mark if the first row and first column need to be set to zero
        # first_row_has_zero = False
        # first_col_has_zero = False

        # # Check if the first row has any zeroes
        # for j in range(n):
        #     if matrix[0][j] == 0:
        #         first_row_has_zero = True

        # # Check if the first column has any zeroes
        # for i in range(m):
        #     if matrix[i][0] == 0:
        #         first_col_has_zero = True

        first_row_has_zero = any(matrix[0][j] == 0 for j in range(len(matrix[0])))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(len(matrix)))

        # Use the first row and column as markers, mark rows and columns that should be zeroed
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out cells based on markers in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out the first row if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero out the first column if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0

# Example usage:
matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

sol = Solution()
print("Input matrix1:")
for row in matrix1:
    print(row)
sol.setZeroes(matrix1)
print("\nOutput matrix1:")
for row in matrix1:
    print(row)

print("\nInput matrix2:")
for row in matrix2:
    print(row)
sol.setZeroes(matrix2)
print("\nOutput matrix2:")
for row in matrix2:
    print(row)
