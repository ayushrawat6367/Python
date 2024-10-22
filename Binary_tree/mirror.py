# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def is_mirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False

            if t1.val != t2.val:
                return False
            
            return is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

        return is_mirror(root.left, root.right)

# Example usage:
if __name__ == "__main__":
    # Creating a symmetric tree: [1, 2, 2, 3, 4, 4, 3]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)

    # Creating a non-symmetric tree: [1, 2, 2, null, 3, null, 3]
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)

    solution = Solution()
    #Root 1
    print(solution.isSymmetric(root1))

    #Root 2
    print(solution.isSymmetric(root2))
