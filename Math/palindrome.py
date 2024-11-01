class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Convert number to string and check if it's equal to its reverse
        return str(x) == str(x)[::-1]
    

# Test cases
#1
print(Solution().isPalindrome(121))
#2
print(Solution().isPalindrome(-121))
#3
print(Solution().isPalindrome(10))

