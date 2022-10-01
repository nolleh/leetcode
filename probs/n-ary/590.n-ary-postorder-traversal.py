class Solution:
    def postorder(self, root:'Node') -> List[int]:
        if root is None:
            return []
       
        # post order: child -> me
        stack, output = [root,], []

        while stack:
            root = stack.pop();
            if root is not None:
                output += [root.val]
            stack += [x for x in root.children]
        return output[::-1]
            
