# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ret = [None]
        def LCA(root):
            if not root:
                return
            if root.val < p.val and root.val < q.val:
                LCA(root.right)
            elif root.val > p.val and root.val > q.val:
                LCA(root.left)
            else:
                ret[0] = root 
                return
        LCA(root)
        return ret[0]