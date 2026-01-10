from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == right:
            return head

        # Dummy node to handle edge case when left=1
        dummy = ListNode(0)
        dummy.next = head

        # Step 1: Move to position left-1
        prev_node = dummy
        for _ in range(left - 1):
            prev_node = prev_node.next

        # Now prev_node.next is at position 'left'
        reverse_start = prev_node.next
        prev = None
        curr = reverse_start

        # Step 2: Reverse from left to right
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Reconnect
        # prev = head of reversed part (position right)
        # curr = node after position right
        # reverse_start = tail of reversed part (original position left)

        prev_node.next = prev  # Connect left-1 to reversed head
        reverse_start.next = curr  # Connect reversed tail to right+1

        return dummy.next
