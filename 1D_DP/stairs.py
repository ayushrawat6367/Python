class Solution:

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        prev1, prev2 = 1, 2
        
        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        
        return prev2
## Time complexity - O(n)
## Space complexity - O(1)


        # if n == 1 or n == 2:
        #     return n
        
        # # Initialize the base cases
        # dp = [0] * (n + 1)
        # dp[1] = 1
        # dp[2] = 2
        
        # # Fill the dp array using the recurrence relation
        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        
        # return dp[n]
## Time complexity - O(n)
## Space complexity - O(n)

# Examples:

#1
print(Solution().climbStairs(2))

#2
print(Solution().climbStairs(3))