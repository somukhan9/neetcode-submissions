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

            res = 0
            if root.val >= maxsofar:
                res = 1
                maxsofar = root.val

            res += dfs(root.left, maxsofar)
            res += dfs(root.right, maxsofar)

            return res


        return dfs(root, root.val)