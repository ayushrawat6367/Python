from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for w in wordDict:
                start = i - len(w)
                if start >=0 and dp[start] and s[start:i] == w:
                    dp[i] = True
                    break
        return dp[-1]
        

#Example 1
s = "leetcode" 
wordDict = ["leet","code"]
print(Solution().wordBreak(s, wordDict))

#Example2
s = "applepenapple"
wordDict = ["apple","pen"]
print(Solution().wordBreak(s, wordDict))

#Example 3
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(Solution().wordBreak(s, wordDict))

