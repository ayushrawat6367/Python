class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) <= 1:
            return s

        max_len = 1
        result = s[0]
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if j - i + 1 > max_len and s[i:j+1] == s[i:j+1][::-1]:
                    max_len = j-i+1
                    result = s[i:j+1]
        return result

#Example 1:
s = "babad"
print(Solution().longestPalindrome(s))


#Example 2
s = "cbbd"
print(Solution().longestPalindrome(s))
