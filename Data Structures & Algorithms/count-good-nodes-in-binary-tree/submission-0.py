# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxsofar):
            if not root:
                return 0

            goodcount = 0
            if root.val >= maxsofar:
                goodcount = 1
                maxsofar = root.val

            leftcount = dfs(root.left, maxsofar)
            rightcount = dfs(root.right, maxsofar)

            return goodcount + leftcount + rightcount


        return dfs(root, root.val)