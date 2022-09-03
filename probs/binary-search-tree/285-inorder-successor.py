class Solution:
    # returns subtrees last node
    previous = None
    inorder_successor_node = None
    
    def iter(self, node:TreeNode, p:TreeNode):
        if not node:
            return
        self.iter(node.left, p)
        
        if self.previous == p and not self.inorder_successor_node:
            self.inorder_successor_node = node
            return
        
        self.previous = node
        self.iter(node.right, p)
       
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # in order: left -> node -> right
        self.iter(root, p)
        return self.inorder_successor_node

