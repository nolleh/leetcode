class Solution:
    def inorderSuccessorWhenHasRight(
        self, node: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if node.right is None:
            return None
        leftmost = node.right
        while leftmost.left:
            leftmost = leftmost.left
        return leftmost

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        node = root
        if node.val == key:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = self.inorderSuccessorWhenHasRight(node)
            node.val = successor.val
            node.right = self.deleteNode(node.right, successor.val)
        elif node.val < key:
            node.right = self.deleteNode(node.right, key)
        else:
            node.left = self.deleteNode(node.left, key)
        return root
