from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        total_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            total_sum += nums[right]

            while total_sum >= target:
                min_length = min(min_length, right - left + 1)
                total_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0
        

target = 7 
nums = [2,3,1,2,4,3]
sol = Solution()
print(sol.minSubArrayLen(target, nums))

target = 4 
nums = [1,4,4]
sol = Solution()
print(sol.minSubArrayLen(target, nums))

target = 11
nums = [1,1,1,1,1,1,1,1]
print(Solution().minSubArrayLen(target, nums))