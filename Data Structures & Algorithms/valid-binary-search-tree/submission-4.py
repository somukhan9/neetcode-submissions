# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def dfs(node: Optional[TreeNode], left: int, right: int) -> bool:
#             if not node:
#                 return True
            
#             if not (left < node.val < right):
#                 return False

#             isBst = dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

#             return isBst

#         return dfs(root, float('-inf'), float('inf'))

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = False
        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            node, left, right = queue.popleft()
            if not (left < node.val < right):
                return False

            if node.left:
                queue.append((node.left, left, node.val))
            if node.right:
                queue.append((node.right, node.val, right))
            

        return True