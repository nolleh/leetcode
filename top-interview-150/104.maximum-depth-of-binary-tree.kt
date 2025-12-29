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
    fun maxDepth(root: TreeNode?): Int {
        val q = ArrayDeque<TreeNode>()
        root?.let { q.add(it) }
        var depth = 0

        // bfs
        while (q.isNotEmpty()) {
            for (i in 0 until q.size) {
                val node = q.removeFirst()
                if (node.left != null) q.add(node.left)
                if (node.right != null) q.add(node.right)
            }
            depth++
        }

        return depth
    }

    fun maxDepth2(root: TreeNode?): Int {
        root ?: return 0
        return 1 + maxOf(maxDepth2(root.left), maxDepth2(root.right))
    }
}

