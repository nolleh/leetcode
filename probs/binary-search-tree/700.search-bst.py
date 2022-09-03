class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node and node.val != val:
            if val < node.val:
                node = node.left
            else:
                node = node.right
                
        return node
 

    def searchBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        
        if val < root.val:
            return self.searchBST2(root.left, val)
        return self.searchBST2(root.right, val)
