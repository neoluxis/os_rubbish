from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Binary Tree Inorder Traversal (LeetCode 94)"""
        res: List[int] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res


# Iterative version (optional)
# def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#     res, stack = [], []
#     curr = root
#     while curr or stack:
#         while curr:
#             stack.append(curr)
#             curr = curr.left
#         curr = stack.pop()
#         res.append(curr.val)
#         curr = curr.right
#     return res