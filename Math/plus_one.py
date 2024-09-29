from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        ##String conversion approach
        # n = int(''.join(map(str, digits)))
        # n += 1
        # return [int(i) for i in str(n)]

        ## Iterative approach
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
        return [1] + digits
    
#Example 1    
digits = [1,2,3]    
print(Solution().plusOne(digits))

#2
digits = [4,3,2,1]    
print(Solution().plusOne(digits))

#3
digits = [9]    
print(Solution().plusOne(digits))
        