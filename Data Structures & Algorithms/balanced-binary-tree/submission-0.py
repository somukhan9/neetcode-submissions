# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def _is_balance(root: TreeNode = None) -> bool:
            if not root:
                return True

            def _height(inner_root: TreeNode) -> int:
                if not inner_root:
                    return 0
                return 1 + max(_height(inner_root.left), _height(inner_root.right))

            left = _height(root.left)
            right = _height(root.right)
            if abs(left - right) > 1:
                return False

            return _is_balance(root.left) and _is_balance(root.right)

        return _is_balance(root)