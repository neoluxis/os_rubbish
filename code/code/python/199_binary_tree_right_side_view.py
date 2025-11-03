from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the values of the nodes you can see ordered from top to bottom
        when standing on the right side of a binary tree.
        """
        if not root:
            return []

        result: List[int] = []
        queue: deque[TreeNode] = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                # Add the last node of the current level to the result
                if i == level_size - 1:
                    result.append(node.val)
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result