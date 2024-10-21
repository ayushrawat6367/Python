class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case for exponent 0
        if n == 0:
            return 1.0
        
        # Handle negative exponent by taking reciprocal
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        current_product = x
        
        while n > 0:
            # If n is odd, multiply the result by current product
            if n % 2 == 1:
                result *= current_product
            
            # Square the current product for the next iteration
            current_product *= current_product
            n //= 2  # Divide n by 2 (integer division)
        
        return result

#Example 1
x = 2.00000
n = 10
print(Solution().myPow(x, n))

#Example 2
x = 2.10000
n = 3
print(Solution().myPow(x, n))

#Example 3
x = 2.00000
n = -2
print(Solution().myPow(x, n))