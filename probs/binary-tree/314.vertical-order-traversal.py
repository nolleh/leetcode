# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 1. put colomns 
        self.minimum = 0
        self.maximum = 0
        ziped: List[(int, int)] = []
        ziped = self.dfs(root, 0, 0)
        #print(ziped)
        length = self.maximum - self.minimum if self.minimum < 0 else self.maximum 
        res = [[] for _ in range(length + 1)]
          
        #print(ziped, self.minimum, self.maximum, length)
        if len(ziped) == 0:
            return []
        for z in ziped:
            #print(res, z, z[1], z[0], res[z[1]+ abs(self.minimum)])
            res[z[2] + abs(self.minimum)] += [(z[0], z[1])]
            vals = res[z[2] + abs(self.minimum)] 
            #print('1:', vals)
            vals = sorted(vals, key = lambda x: x[1])
            #print(vals)
            res[z[2] + abs(self.minimum)] = vals
            #print('2:', vals, list(map(lambda x: x[0], vals)))
        for i,z in enumerate(res):   
            res[i] = list(map(lambda x: x[0], z))
        return res
    
    def dfs(self, node: Optional[TreeNode], depth: int, column: int):
        if node is None:
            return []
        self.minimum = min(self.minimum, column)
        self.maximum = max(self.maximum, column)
        return [(node.val, depth, column)] + self.dfs(node.left, depth + 1, column - 1) + self.dfs(node.right, depth + 1, column + 1) 
        
