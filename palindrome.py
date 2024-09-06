class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(char.lower() for char in s if char.isalnum())

        if new_s == new_s[::-1]:
            return True
        return False
    
s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))

s = "race a car"
print(Solution().isPalindrome(s))

