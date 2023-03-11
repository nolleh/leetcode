# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder : left -> root -> right
        # if root is None:
        #    return []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        stack = []
        curr = root
        output = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            output.append(curr.val)
            curr = curr.right
        return output
