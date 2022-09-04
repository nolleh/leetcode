class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([root])
        levels = []
        level = 0
        while queue:
            levels.append([]) 
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
            level +=1
        return levels
        
