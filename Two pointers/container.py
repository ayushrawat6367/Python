from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the current area
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height
            # Update the maximum area found so far
            max_area = max(max_area, area)
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area

##Example

height = [1,8,6,2,5,4,8,3,7]

sol = Solution()
print(sol.maxArea(height))

height = [1,1]
sol = Solution()
print(sol.maxArea(height))