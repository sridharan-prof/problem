#User function Template for python3

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
# Note: Build tree and return root node
class Solution:
    def buildTree(self, inorder, preorder):
        # code here
        if not preorder or not inorder:
            return None

        root_val = preorder.pop(0)  # Root node from preorder
        root = Node(root_val)
        inorder_index = inorder.index(root_val)

        # Recursively build left and right subtrees
        root.left = self.buildTree(inorder[:inorder_index], preorder)
        root.right = self.buildTree(inorder[inorder_index + 1:], preorder)

        return root

    def postorderTraversal(self, root, result):
        if root:
            self.postorderTraversal(root.left, result)
            self.postorderTraversal(root.right, result)
            result.append(root.data)

    def getPostorder(self, inorder, preorder):
        root = self.buildTree(inorder, preorder)
        result = []
        self.postorderTraversal(root, result)
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        inorder = [int(x) for x in input().split()]
        preorder = [int(x) for x in input().split()]

        root = Solution().buildTree(inorder, preorder)
        printPostorder(root)
        print()

# } Driver Code Ends