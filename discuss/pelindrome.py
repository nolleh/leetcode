# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
      def reverse(node): # O(n)
        prev = None
        while node: # while node avail
          next_node = node.next 
          node.next = prev # next as prev
          prev, node = node, next_node 
                
        return prev
        
      slow = head
      fast = head.next
      while fast and fast.next: # has also next
        slow = slow.next 
        fast = fast.next.next # fast is twice of slow
        
      n1 = head
      n2 = reverse(slow.next) # cause while statements end until fast.next is not avail and it's twice faster compared with slow,
      # so, when list is started with [1,2,4,4,1] 
      # fast 2 -> 4 (3) 
      # slow is 1 -> 2
      
      # when list is started with [1,2,2,1]
      # fast 2(1) -> 1
      # slow 1 -> 2(1)
      
      # in short, we devide list two parts, only with time : O(n), storage: O(1)
      # 
      while n2: # traverse reversed slow
        if n1.val != n2.val: # if not same
            return False # not pelindrome
            
        n1 = n1.next
        n2 = n2.next
            
      return True # pelinedrom
