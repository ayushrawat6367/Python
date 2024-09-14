class Solution:

    def customSortString(self, order: str, s: str) -> str:
        # Create a dictionary that stores the index of each character in `order`
        order_map = {char: i for i, char in enumerate(order)}
        
        # Divide the characters of `s` into two groups: those in `order` and those not in `order`
        in_order = []
        not_in_order = []
        
        for char in s:
            if char in order_map:
                in_order.append(char)
            else:
                not_in_order.append(char)
        
        # Sort the characters in `in_order` based on their index in `order_map`
        in_order.sort(key=lambda x: order_map[x])
        
        # Combine the sorted `in_order` characters with `not_in_order`
        return ''.join(in_order) + ''.join(not_in_order)

# Example usage

order = "cba"
s = "abcd"
print(Solution().customSortString(order, s))

print(Solution().customSortString("bcafg", "abcd"))
