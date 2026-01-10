from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            if not root:
                return True

            if root.val <= min_val or root.val >= max_val:
                return False

            left = helper(root.left, min_val, root.val)
            right = helper(root.right, root.val, max_val)

            return left and right

        return helper(root, float("-inf"), float("inf"))
