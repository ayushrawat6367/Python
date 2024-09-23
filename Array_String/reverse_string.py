def reverseWords(s: str) -> str:
    words = s.split()
    
    reversed_words = words[::-1]
    
    return ' '.join(reversed_words)

# Example 1
s1 = "the sky is blue"
print(reverseWords(s1))

# Example 2
s2 = "  hello world  "
print(reverseWords(s2))

# Example 3
s3 = "a good   example"
print(reverseWords(s3))
