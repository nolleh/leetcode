/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        // Use dummy head to simplify the logic
        val dummyHead = ListNode(0)
        var current = dummyHead
        var node1 = l1
        var node2 = l2
        var carry = 0

        // Continue while there are nodes in either list or carry exists
        while (node1 != null || node2 != null || carry != 0) {
            // Get values from nodes, default to 0 if node is null
            val val1 = node1?.`val` ?: 0
            val val2 = node2?.`val` ?: 0

            // Calculate sum and carry
            val sum = val1 + val2 + carry
            carry = sum / 10
            val digit = sum % 10

            // Create new node with the digit
            current.next = ListNode(digit)
            current = current.next!!

            // Move to next nodes
            node1 = node1?.next
            node2 = node2?.next
        }

        return dummyHead.next
    }
}

