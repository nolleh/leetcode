class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = {}
        prv = None
        node = head
        while node:
            if node.val in nodes:
                prv.next = node.next
            else:
                nodes[node.val] = node
                prv = node
            node = node.next
        return head
