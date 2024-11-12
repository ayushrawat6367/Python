class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # If the root is None, there is no path
        if not root:
            return False
        
        # If the current node is a leaf, check if the targetSum matches its value
        if not root.left and not root.right:
            return targetSum == root.val
        
        targetSum -= root.val
        
        return (self.hasPathSum(root.left, targetSum) or 
                self.hasPathSum(root.right, targetSum))

def build_tree(nodes, index=0):
    if index >= len(nodes) or nodes[index] is None:
        return None
    root = TreeNode(nodes[index])
    root.left = build_tree(nodes, 2 * index + 1)
    root.right = build_tree(nodes, 2 * index + 2)
    return root

#Examples
if __name__ == "__main__":
    tree1 = build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    solution = Solution()
    print("Example 1: ", solution.hasPathSum(tree1, 22)) 

    # Example 2: root = [1,2,3], targetSum = 5
    tree2 = build_tree([1,2,3])
    print("Example 2: ", solution.hasPathSum(tree2, 5))

    # Example 3: root = [], targetSum = 0
    tree3 = build_tree([])
    print("Example 3: ", solution.hasPathSum(tree3, 0))
