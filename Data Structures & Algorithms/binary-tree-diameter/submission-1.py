# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         def _height(root: TreeNode) -> int:
#             if not root:
#                 return 0
#             return 1 + max(_height(root.left), _height(root.right))

#         left_height = _height(root.left)
#         right_height = _height(root.right)
#         diameter = left_height + right_height
#         sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

#         return max(diameter, sub)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def _height(root: TreeNode) -> int:
            nonlocal res

            if not root:
                return 0

            left_height = _height(root.left)
            right_height = _height(root.right)

            res = max(res, left_height + right_height)

            return 1 + max(left_height, right_height)

        _height(root)
        return res