# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        result = []

        queue = deque([root])

        while queue:
            level = []
            size = len(queue)

            for _ in range(size):
                p = queue.popleft()
                level.append(p.val)

                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)

            result.append(level[-1])

        return result