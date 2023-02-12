# Medium
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
        if not root:
            return root

        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
                leftmost = leftmost.left
        return root


#     # perfect binary tree is always 2^n + 1
#     # where n is level
#     self.track(root, None, 1, True)
#     return root
#
# def track(self, node: 'Optional[Node]', parent: 'Optional[Node]', level: int, amIRightChild: bool):
#   if not node:
#     return
#
#   if not amIRightChild: # leftnode
#     node.next = parent.right
#   elif parent and not parent.right:
#     node.next = None
#   elif parent:
#     node.next = parent.next.left if parent.next else None
#   if node.left:
#     self.track(node.left, node, level+1, False)
#   if node.right:
#     self.track(node.right, node, level+1, True)

## ---------
## LEVEL ORDER TRAVERSAL
## Solution
## while (!Q.empty())
## {
##     size = Q.size()
##     for i in range 0..size
##     {
##         node = Q.pop()
##         Q.push(node.left)
##         Q.push(node.right)
##     }
## }
##
##
##
# 1. Makes Queue. (Tuple, NULL, nested loop)
# 2. adding root of the tree in the queue (1) -> (2,3)/ 1 was poped
# 3. first while loop iterates over each level one by one and and the inner loop over all the nodes
# 4. (2,3) -> (3, 4, 5). also, the element at the head of the queue is the `next element` in order.
# 5. (3, 4, 5) -> (4, 5, 6, 7)
###
"""
import collections 

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # Initialize a queue data structure which contains
        # just the root of the tree
        Q = collections.deque([root])
        
        # Outer while loop which iterates over 
        # each level
        while Q:
            
            # Note the size of the queue
            size = len(Q)
            
            # Iterate over all the nodes on the current level
            for i in range(size):
                
                # Pop a node from the front of the queue
                node = Q.popleft()
                
                # This check is important. We don't want to
                # establish any wrong connections. The queue will
                # contain nodes from 2 levels at most at any
                # point in time. This check ensures we only 
                # don't establish next pointers beyond the end
                # of a level
                if i < size - 1:
                  node.next = Q[0]
                
                # Add the children, if any, to the back of
                # the queue
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        # Since the tree has now been modified, return the root node
        return root
"""
