class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0 || inorder.length == 0) return null;
        // preorder = node -> lefts -> rights 
        // inorder = lefts -> node -> rights
        int node = preorder[0];
        int N = preorder.length;
        
        int L = IntStream.range(0, inorder.length)
            .filter(i -> inorder[i] == node).findFirst().orElse(-1);

        if (L < 0) return null;
        
        // for lefts, reconstruct 
        TreeNode left = buildTree(Arrays.copyOfRange(preorder, 1, L+1), Arrays.copyOfRange(inorder, 0, L));
        TreeNode right = buildTree(Arrays.copyOfRange(preorder, L+1, N), Arrays.copyOfRange(inorder, L+1, N));
        return new TreeNode(node, left, right);
    }
}
