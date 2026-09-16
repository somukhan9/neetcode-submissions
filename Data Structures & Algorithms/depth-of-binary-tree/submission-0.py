# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def _depth(root: TreeNode) -> int:
            if not root:
                return 0
            return 1 + max(_depth(root.left), _depth(root.right))
        return _depth(root)