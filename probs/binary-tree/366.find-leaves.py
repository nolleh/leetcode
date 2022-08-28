from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        p = root
        while p:
            this_time, p = self.leaves(root, None, False)
            res += [this_time]
        return res    
       
    def leaves(self, node: Optional[TreeNode], p: Optional[TreeNode], is_left: bool) -> (List[int], Optional[TreeNode]):
        if node is None:
            return [], node
        
        if node.left is None and node.right is None:
            if p is not None:
                if is_left:
                    p.left = None
                else:
                    p.right = None
            return [node.val], p
        return self.leaves(node.left, node, True)[0] + self.leaves(node.right, node, False)[0], node
