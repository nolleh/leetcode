class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursive 
        if root1 is None and root2 is None:
           return None
        
        val = (root1.val if root1 else 0) + (root2.val if root2 else 0)
        left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None) 
        right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        return TreeNode(val, left, right)
        
        # iterative
        #if not root1:
        #    return root2
        #
        #stack = [(root1, root2)]
        #while stack:
        #    (s1,s2) = stack.pop()
        #    if (not s1) or (not s2):
        #        continue
        #    
        #    s1.val += s2.val
        #    if not s1.left:
        #        s1.left = s2.left
        #    else:
        #        stack += [(s1.left, s2.left)]
        #    if not s1.right:
        #        s1.right = s2.right
        #    else:
        #        stack += [(s1.right, s2.right)]
        #return s1
