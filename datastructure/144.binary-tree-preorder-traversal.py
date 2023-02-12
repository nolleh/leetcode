# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # preorder: root -> left -> right
        # ---- recursive
        # if root is None:
        #     return []
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

        # ----iterative
        if root is None:
            return []
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            # print(list(map(lambda x: x.val, q)))
            node = q.popleft()
            res += [node.val]
            # [root.val, left1, left1.left, left1.right]
            # pop left, push left to mychilds
            if node.right:
                q.appendleft(node.right)
            if node.left:
                q.appendleft(node.left)
        return res
