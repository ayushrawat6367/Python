from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Step 1: Sort the citations array in descending order
        citations.sort(reverse=True)
        
        # Step 2: Initialize h-index to 0
        h = 0
        
        # Step 3: Iterate over the sorted array and determine the h-index
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h = h + 1
            else:
                break
        
        return h

solution = Solution()

# Example 1
citations1 = [3, 0, 6, 1, 5]
print(solution.hIndex(citations1))  # Output: 3

# Example 2
citations2 = [1, 3, 1]
print(solution.hIndex(citations2))  # Output: 1