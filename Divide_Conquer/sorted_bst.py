# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    # Base case: if the array is empty, return None
    if not nums:
        return None
    
    # Find the middle index
    mid = len(nums) // 2
    
    # Create a TreeNode with the middle value
    root = TreeNode(nums[mid])
    
    # Recursively create the left subtree from the left subarray
    root.left = sortedArrayToBST(nums[:mid])
    
    # Recursively create the right subtree from the right subarray
    root.right = sortedArrayToBST(nums[mid+1:])
    
    return root

# Helper function to print the tree in level-order (to visualize it)
from collections import deque

def printTree(root):
    if not root:
        return "[]"
    
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
    
    # Remove trailing None values for a cleaner output
    while result and result[-1] is None:
        result.pop()
    
    return result

nums1 = [-10, -3, 0, 5, 9]
nums2 = [1, 3]

bst1 = sortedArrayToBST(nums1)
bst2 = sortedArrayToBST(nums2)

# Output the results
print(printTree(bst1))
print(printTree(bst2))
