# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invTree(root):
            if not root:
                return 
            l = invTree(root.right)
            r = invTree(root.left)
            return TreeNode(root.val, left = l, right =r)
        return invTree(root)