class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        now = head
        length = 0
        while now:
            length += 1
            now = now.next
        now = head

        # addition = 0 if length % 2 else 1 # len is odd: 0, even: 1
        addition = 0
        for i in range(length // 2 + addition):
            now = now.next

        return now
