class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        now = head
        p = None
        
        while now:
            next = now.next # next = 2.next (3)
            now.next = p # 2.next = p (1)
            p = now # p = now 
            now = next
        return p
            
        
