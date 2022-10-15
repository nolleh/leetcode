"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        ## recursive 
		#if not root:
        #    return 0 
        
        #return 1 + max([self.maxDepth(c) for c in root.children] if root.children else [0]
		## iterative
		stack = [(root, 1)]
        maxlen = 0
        while stack:
            node, depth = stack.pop()
            if node:
                maxlen = max(maxlen, depth)
                for c in node.children:
                    stack += [(c, depth + 1)]
            
        return maxlen

