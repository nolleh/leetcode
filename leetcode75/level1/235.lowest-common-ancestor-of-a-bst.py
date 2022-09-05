class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        def getPath(node: TreeNode, t: TreeNode): 
            # python has no tail-recursion opt.
            # so just put in here, but having habit for tail-rec will be great.
            if not node:
                return []
            if t.val == node.val:
                return [node]
            elif t.val < node.val:
                return [node] + getPath(node.left, t)
            return [node] + getPath(node.right, t) 
        # LCA: p and q as lowest node in T that has both p and q as descendants
        # 'a node can be descendant of itself'
        ppath = getPath(root, p) 
        qpath = getPath(root, q)
        # print('------')
        # print(list(map(lambda x: x.val, ppath)), list(map(lambda x: x.val, qpath)))
        for p in reversed(ppath):
            for q in reversed(qpath):
                if q == p:
                    return q
        
        return None
        """
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        ## if both p and q are bigger, then go to right
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        ## if both p and q are smaller than parent, then go to left
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        ## by bst's property, if the compare result was different, meaning 'this node is LCA'
        else:
            return root
        
