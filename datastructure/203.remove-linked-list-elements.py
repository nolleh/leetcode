class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = head
        prv = None
        while node:
            if node.val == val:
                if prv:
                    prv.next = node.next
                else:
                    head = head.next
                    node = node.next
                    continue
            else:
                prv = node
            node = node.next
        return head
