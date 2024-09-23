from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result array with 1's
        answer = [1] * len(nums)
        
        # First pass: calculate the products of all elements to the left of each element
        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]
        
        # Second pass: calculate the products of all elements to the right of each element
        R = 1  # R is the product of all elements to the right of the current element
        for i in reversed(range(len(nums))):
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer


solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
