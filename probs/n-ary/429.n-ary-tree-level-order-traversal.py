from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        q += [root]
        
        output = []
        while q:
            level = []
            # how to check, am I level's last node?
            # use size of q.
            # next iteration, we'll remove all the children from the queue 
            size = len(q)
            for _ in range(size):
                node = q.popleft() 
                level += [node.val]
                q += [x for x in node.children]
            output += [level]
        return output 
