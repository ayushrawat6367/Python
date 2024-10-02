## Solution 1 - Dynamic programming (Time complexity - O(n.m), Spcace complexity - O(1))
def find_largest_square(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    max_size = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:  # Only consider cells that are 1
                if i == 0 or j == 0:
                    dp[i][j] = 1  # The first row or first column can only have squares of size 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1  # Fill the dp table
                max_size = max(max_size, dp[i][j])  # Update the maximum size found

    return max_size

# ## Solution 2 - Brute Force (Time complexity - O(n^2.m^2), Spcace complexity - O(1))
# def find_largest_square(matrix):
#     if not matrix or not matrix[0]:
#         return 0

#     rows = len(matrix)
#     cols = len(matrix[0])
#     max_size = 0

#     # Iterate through each cell in the matrix
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == 1:  # Start only if the cell is 1
#                 # Initialize size of the square
#                 size = 1
                
#                 # Check for maximum square size
#                 while (i + size < rows) and (j + size < cols):
#                     # Check if the new square is valid
#                     valid_square = True
#                     for k in range(size + 1):  # Check the new row and new column
#                         if matrix[i + size][j + k] == 0 or matrix[i + k][j + size] == 0:
#                             valid_square = False
#                             break
                    
#                     if valid_square:
#                         size += 1
#                     else:
#                         break

#                 max_size = max(max_size, size)

#     return max_size


# Example usage
matrix = [
    [1, 1, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0]
]

print(find_largest_square(matrix))  # Expected output: 3
