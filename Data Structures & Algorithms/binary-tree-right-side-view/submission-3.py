# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque([root])

        while queue:
            size = len(queue)
            rightmost = None
            for _ in range(size):
                p = queue.popleft()

                if p:
                    rightmost = p

                    if p.left:
                        queue.append(p.left)
                    if p.right:
                        queue.append(p.right)
            
            if rightmost:
                result.append(rightmost.val)

        return result