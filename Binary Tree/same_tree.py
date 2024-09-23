# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # If both trees are empty, they are the same
        if not p and not q:
            return True
        # If one tree is empty and the other is not, they are not the same
        if not p or not q:
            return False
        # If the values of the current nodes are different, they are not the same
        if p.val != q.val:
            return False
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Helper function to build a binary tree from a list (level-order insertion)
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        current = queue.pop(0)
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

# Example usage:

#1
p = build_tree([1, 2, 3])
q = build_tree([1, 2, 3])
solution = Solution()
print(solution.isSameTree(p, q))

#2
p = build_tree([1, 2])
q = build_tree([1, None, 2])
print(solution.isSameTree(p, q))

#1
p = build_tree([1, 2, 1])
q = build_tree([1, 1, 2])
print(solution.isSameTree(p, q))
