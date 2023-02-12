class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list2 is None:
            return list1
        if list1 is None:
            return list2
        if list1.val > list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
