class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.prev = None  # To store the previous node value during in-order traversal
        self.min_diff = float('inf')  # Initialize min_diff with infinity
        
        def inorder(node):
            if node is None:
                return  # Base case: Stop recursion if the node is None
            
            # Traverse the left subtree
            inorder(node.left)
            
            # Process the current node
            if self.prev is not None:
                current_diff = node.val - self.prev
                self.min_diff = min(self.min_diff, current_diff)
                print(f"Current Node: {node.val}, Previous Node: {self.prev}, "
                      f"Current Difference: {current_diff}, Minimum Difference: {self.min_diff}")
            else:
                print(f"Current Node: {node.val}, Previous Node: None (first node)")
            
            self.prev = node.val  # Update previous node value
            
            # Traverse the right subtree
            inorder(node.right)
        
        # Perform in-order traversal of the BST
        inorder(root)
        return self.min_diff

# Example Test Cases
if __name__ == "__main__":
    # Test case 1: root = [4, 2, 6, 1, 3]
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(6)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)

    print("Test Case 1:")
    solution = Solution()
    result1 = solution.getMinimumDifference(root1)
    print(f"Final Minimum Difference: {result1}\n")

    # Test case 2: root = [1, 0, 48, None, None, 12, 49]
    root2 = TreeNode(1)
    root2.left = TreeNode(0)
    root2.right = TreeNode(48)
    root2.right.left = TreeNode(12)
    root2.right.right = TreeNode(49)

    print("Test Case 2:")
    result2 = solution.getMinimumDifference(root2)
    print(f"Final Minimum Difference: {result2}")
