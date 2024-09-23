from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Step 1: Transpose the matrix (swap rows and columns)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()

# Example usage
if __name__ == "__main__":
    # 2D matrix representing an image
    image_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # Print original matrix
    print("Original Matrix:")
    for row in image_matrix:
        print(row)
    
    # Rotate the matrix 90 degrees clockwise
    solution = Solution()
    solution.rotate(image_matrix)
    
    # Print rotated matrix
    print("\nRotated Matrix:")
    for row in image_matrix:
        print(row)
