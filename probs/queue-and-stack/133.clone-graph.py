"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        def iter(curr: "Node"):
            copy[curr] = Node(curr.val)
            for n in curr.neighbors:
                if n not in copy:
                    iter(n)
                # eventhough already visit, add connection
                copy[curr].neighbors.append(copy[n])

        if not node:
            return node
        copy = {}
        iter(node)
        return copy[node]
