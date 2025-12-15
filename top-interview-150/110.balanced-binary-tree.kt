/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun isBalanced(root: TreeNode?): Boolean {
        root ?: return true

        // Helper function that returns the height of the tree
        // Returns -1 if the tree is unbalanced (as a sentinel value)
        fun getHeight(node: TreeNode?): Int {
            node ?: return 0

            val leftHeight = getHeight(node.left)
            // If left subtree is unbalanced, propagate the -1 up
            if (leftHeight == -1) return -1

            val rightHeight = getHeight(node.right)
            // If right subtree is unbalanced, propagate the -1 up
            if (rightHeight == -1) return -1

            // Check if current node is balanced
            if (kotlin.math.abs(leftHeight - rightHeight) > 1) return -1

            // Return the height of current node
            return maxOf(leftHeight, rightHeight) + 1
        }

        return getHeight(root) != -1
    }
}

// Alternative approach: Separate the height calculation and balance check
// class Solution {
//     fun isBalanced(root: TreeNode?): Boolean {
//         root ?: return true
//
//         fun getHeight(node: TreeNode?): Int {
//             node ?: return 0
//             return maxOf(getHeight(node.left), getHeight(node.right)) + 1
//         }
//
//         // Check if current node is balanced AND recursively check subtrees
//         val heightDiff = kotlin.math.abs(getHeight(root.left) - getHeight(root.right))
//         return heightDiff <= 1 &&
//                isBalanced(root.left) &&
//                isBalanced(root.right)
//     }
// }

