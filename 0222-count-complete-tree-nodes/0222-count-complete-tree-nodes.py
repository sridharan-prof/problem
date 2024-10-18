# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        result = []
        def traversal(node):
            if node is None:
                return 0
            traversal(node.left)
            traversal(node.right)
            result.append(node.val)
        traversal(root)
        return len(result)
        