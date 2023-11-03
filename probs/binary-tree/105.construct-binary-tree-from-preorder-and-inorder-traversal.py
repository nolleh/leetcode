class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = node, lefts, rights
        # inorder = left, node, rights

        if len(preorder) == 0 or len(inorder) == 0:
            return
        N = len(preorder)
        node = preorder[0]
        if node not in inorder:
            return
        L = inorder.index(node)

        return TreeNode(
            node,
            self.buildTree(preorder[1:], inorder[: L + 1]),
            self.buildTree(preorder[L + 1 :], inorder[L + 1 :]),
        )
