class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = {} 
        node = head
        while node:
            if node in nodes:
                return True
            nodes[node] = node
            node = node.next
        return False
