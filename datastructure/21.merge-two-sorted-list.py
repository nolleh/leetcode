# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode(-1)
        lastnode = head
        while list1 or list2:
            if list2 is None or (list1 and list1.val < list2.val):
                # choose curl1
                lastnode.next = list1
                list1 = list1.next
            else:
                lastnode.next = list2
                list2 = list2.next
            lastnode = lastnode.next
        return head.next
