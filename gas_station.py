from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_total = 0
        gas_current = 0
        start = 0

        for i in range(len(gas)):
            gas_current += gas[i] - cost[i]
            gas_total += gas[i] - cost[i]

            if gas_current < 0:
                start = i + 1
                gas_current = 0
        
        return start if gas_total >= 0 else -1
    
sol = Solution()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(sol.canCompleteCircuit(gas, cost)) 