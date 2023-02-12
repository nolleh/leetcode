"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# perfect binary tree :
# 1. all leaves are on same level
# 2. every parent has two children
# Runtime: 129 ms, faster than 16.13% (T^T) of Python3 online submissions for Populating Next Right Pointers in Each Node.
# Memory Usage: 15.5 MB, less than 96.98% of Python3 online submissions for Populating Next Right Pointers in Each Node.
class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        # perfect binary tree is always 2^n + 1
        # where n is level
        self.track(root, None, 1, True)
        return root

    def track(
        self,
        node: "Optional[Node]",
        parent: "Optional[Node]",
        level: int,
        amIRightChild: bool,
    ):
        if not node:
            return

        if not amIRightChild:  # leftnode
            node.next = parent.right
        elif parent and not parent.right:
            node.next = None
        elif parent:
            node.next = parent.next.left if parent.next else None
        if node.left:
            self.track(node.left, node, level + 1, False)
        if node.right:
            self.track(node.right, node, level + 1, True)
