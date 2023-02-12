# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # if not root:
        #     return sys.maxsize
        # if root.val > target:
        #     leftres = self.closestValue(root.left, target)
        #     if abs(leftres - target) < abs(root.val - target):
        #         return leftres
        #     else:
        #         return root.val
        # else:
        #     rightres = self.closestValue(root.right, target)
        #     if abs(rightres - target) < abs(root.val - target):
        #         return rightres
        #     else:
        #         return root.val
        # def inorder(r: TreeNode):
        #    return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        # return min(inorder(root), key = lambda x: abs(target - x))

        closest = root.val
        while root:
            closest = min(root.val, closest, key=lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest
