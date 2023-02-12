class Solution:
    def preorder(self, root: "Node") -> List[int]:
        # return preorder traversal of nodes' values
        # preorder: node -> left to right childs

        # if not root:
        #    return []
        # childs = []
        # for c in root.children:
        #    childs += self.preorder(c)
        # return [root.val] + childs

        if not root:
            return []
        stack, output = [
            root,
        ], []
        while stack:
            root = stack.pop()  # [1] -> [] / [4, 2, 3] -> [4, 2]
            # root = stack[0]
            # stack = stack[1:]
            output.append(root.val)  # [1] / [1, 4]
            # [::-1]: reversed list
            # extend: insert data and if necessary, extends capa
            # because the next levels child need to be poped first
            # before prior level's uncle, it is reversed and poped. if you do not reverse,
            # then you should put child to place prior, meaning replace n+1 data.
            # it looks like no critical diff from former and latters methods, so we choose former method to consice code
            stack.extend(root.children[::-1])  # [4,2,3] / [4,2,6,5]
            # stack.extend(root.children)
        return output
