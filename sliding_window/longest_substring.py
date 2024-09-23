class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # Set to store characters in the current window
        max_len = 0  # Variable to track the maximum length
        start = 0  # Start pointer for the sliding window
        
        for end in range(len(s)):  # End pointer moves through the string
            while s[end] in char_set:
                char_set.remove(s[start])  # Remove the character at the start
                start += 1  # Move start pointer forward
                
            char_set.add(s[end])  # Add the current character to the set

            max_len = max(max_len, end - start + 1)  # Update max length
        
        return max_len
    
##Example
s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))

s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))


s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
