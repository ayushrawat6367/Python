from collections import defaultdict, deque
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Adjacency list for the graph
        outgoing = defaultdict(list)  # Tracks roads from a -> b (as given)
        incoming = defaultdict(list)  # Tracks reverse roads b -> a
        
        # Build the graph with both outgoing and incoming edges
        for a, b in connections:
            outgoing[a].append(b)  # Original direction a -> b
            incoming[b].append(a)   # Reverse direction b -> a
        
        # Use BFS to traverse the graph starting from city 0
        queue = deque([0])
        visited = set([0])
        changes_needed = 0
        
        while queue:
            current_city = queue.popleft()
            
            # Check all outgoing edges (roads that need potential reversal)
            for neighbor in outgoing[current_city]:
                if neighbor not in visited:
                    # If there's an outgoing road from current_city to neighbor,
                    # we need to reverse this road.
                    changes_needed += 1
                    visited.add(neighbor)
                    queue.append(neighbor)
            
            # Check all incoming edges (roads that are already correct)
            for neighbor in incoming[current_city]:
                if neighbor not in visited:
                    # These roads don't need reversal, just visit the city.
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return changes_needed



solution = Solution()
print(solution.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))  # Output: 3
print(solution.minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]))          # Output: 2
