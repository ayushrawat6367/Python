from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Return 1-indexed positions
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1


### Example

numbers = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(numbers, target))

numbers = [2, 3, 4]
target = 6
sol = Solution()
print(sol.twoSum(numbers, target))

numbers = [-1, 0]
target = -1
sol = Solution()
print(sol.twoSum(numbers, target))


