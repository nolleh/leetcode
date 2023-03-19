# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # given the head of a sorted linked list, delete all nodes that have dup numbers.
        if head is None:
            return head

        curr = head
        fast = curr.next
        last = curr if fast and curr and fast.val != curr.val else None
        isDup = False
        while fast:
            if fast.val != curr.val:
                # this val doesn't duplicated.
                if fast.next is None or fast.next.val != fast.val:
                    # first value was duplicated, and this val is acutal first
                    if last is None and head != curr:
                        head = fast
                    elif last:
                        last.next = fast
                    last = fast
                isDup = False
            else:
                isDup = True
            curr = fast
            fast = fast.next
        if isDup:
            if last:
                last.next = None
            else:
                head = None
        return head
