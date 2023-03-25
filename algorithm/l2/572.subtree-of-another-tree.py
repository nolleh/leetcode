# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def iter(fst, snd):
            if not fst and not snd:
                return True
            elif not fst or not snd:
                return False
            elif fst.val != snd.val:
                return False
            return iter(fst.left, snd.left) and iter(fst.right, snd.right)

        if not root:
            return False
        elif iter(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(
                root.right, subRoot
            )
