from typing import List

class CustomFunction:
    # f(x, y) = x + y (for testing)
    def f(self, x: int, y: int) -> int:
        return x + y  # Example function

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        x, y = 1, 1000  # Start with x = 1 and a large y value, as f(x, y) is increasing
        
        # Two-pointer approach
        while x <= 1000 and y >= 1:
            value = customfunction.f(x, y)  # Call f() on the instance `customfunction`
            
            if value == z:
                result.append([x, y])  # Found a valid pair
                x += 1  # Move right to find next potential pair
                y -= 1  # Move up to check if there are more pairs
            elif value < z:
                x += 1  # Move right to increase the value of f(x, y)
            else:
                y -= 1  # Move up to decrease the value of f(x, y)
        
        return result

# Example usage
customfunction = CustomFunction()  # Create an instance of CustomFunction
solution = Solution()

z = 5  # Example target value
result = solution.findSolution(customfunction, z)

# Output the result
print(f"Pairs where f(x, y) == {z}: {result}")
