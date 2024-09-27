# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

# Helper function to print the binary tree level by level (BFS)
from collections import deque

def print_tree(root: TreeNode):
    if not root:
        print("[]")
        return

    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    print(result)

# Example usage
if __name__ == "__main__":
    # Construct the binary tree [4, 2, 7, 1, 3, 6, 9]
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7, TreeNode(6), TreeNode(9))
    
    print("Original Tree:")
    print_tree(root)

    # Invert the binary tree
    solution = Solution()
    inverted_root = solution.invertTree(root)

    print("Inverted Tree:")
    print_tree(inverted_root)
