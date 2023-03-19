class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # node = head
        # len = 0
        # while node:
        #    node = node.next
        #    len +=1
        # if len == 1:
        #    return None
        # i = 0
        # node = head
        # while node:
        #    if len -n - 1 == -1:
        #        return node.next
        #    if len - n -1 == i:
        #        node.next = node.next.next if node.next else None
        #    else:
        #        node = node.next
        #    i+=1
        # return head

        # O(N)
        node_before_delete = head
        for i in range(n):
            node_before_delete = node_before_delete.next

        if not node_before_delete:
            return head.next

        node = node_before_delete
        node_before_delete = head
        while node.next:
            node_before_delete = node_before_delete.next
            node = node.next
        node_before_delete.next = node_before_delete.next.next
        return head
