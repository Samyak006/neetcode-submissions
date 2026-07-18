# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
            dfs: 
                post compute if l+r+curr > 0 
        '''
        maxPath = root.val
        def dfs(root):
            nonlocal maxPath
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            maxPath = max(maxPath, root.val+ max(l,0) + max(r,0))
            return root.val+ max(max(l,0) , max(r,0))
        dfs(root)
        return maxPath