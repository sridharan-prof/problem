# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def isLeaf(node):
            return node is not None and node.left is None and node.right is None
        
        # Recursive function to traverse the tree
        def dfs(node):
            if node is None:
                return 0
            
            left_sum = 0
            # Check if the left child is a leaf
            if node.left and isLeaf(node.left):
                left_sum += node.left.val
            
            # Recursively sum the left leaves from both left and right children
            return left_sum + dfs(node.left) + dfs(node.right)
        
        # Start the DFS traversal from the root
        return dfs(root)
        