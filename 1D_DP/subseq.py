def longest_profit(data):
    n = len(data)
    if n == 0:
        return 0
    
    # Initialize the dp array with 1s, as the smallest increasing subsequence is the element itself
    dp = [1] * n
    
    # Fill dp array
    for i in range(1, n):
        for j in range(i):
            if data[i] > data[j]:  # Increasing condition
                dp[i] = max(dp[i], dp[j] + 1)
    
    # maximum value in dp array
    return max(dp)

# Example usage
print(longest_profit([-1, 9, 0, 8, -5, 6, -24]))
print(longest_profit([1, -4, 5, -3]))
print(longest_profit([-3, -4, -5, -6]))
