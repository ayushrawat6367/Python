from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        # Helper function for backtracking
        def backtrack(current, open_count, close_count):
            # If the current string is complete, add it to the result
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Add an open parenthesis if we haven't used all n open parentheses
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            # Add a close parenthesis if it won't make the parentheses invalid
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        
        # Start the backtracking with an empty string and no parentheses used
        backtrack("", 0, 0)
        
        return result

## Examples
print(Solution().generateParenthesis(3))

print(Solution().generateParenthesis(1))

