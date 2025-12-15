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
    private var prev: Int? = null
    private var minDiff = Int.MAX_VALUE

    fun getMinimumDifference(root: TreeNode?): Int {
        prev = null
        minDiff = Int.MAX_VALUE
        inorderTraverse(root)
        return minDiff
    }

    private fun inorderTraverse(root: TreeNode?) {
        // Kotlin tip: Early return with Elvis operator
        // Instead of: if (root == null) { return }
        //
        // How it works:
        // - Elvis operator: expression ?: alternative
        // - If expression is NOT null: evaluates to expression (but we ignore the value)
        // - If expression IS null: evaluates to alternative (which is 'return' here)
        // - Since 'return' exits the function, this effectively means "if null, return"
        root ?: return

        // In-order traversal: left -> root -> right
        inorderTraverse(root.left)

        // Kotlin tip: Use safe call and let for null checks (avoids !! operator)
        // Instead of: if (prev != null) { minDiff = minOf(minDiff, root.`val` - prev!!) }
        prev?.let {
            minDiff = minOf(minDiff, root.`val` - it)  // 'it' refers to prev
        }
        prev = root.`val`

        inorderTraverse(root.right)
    }
}

// Alternative: Using local variables instead of class properties
// class Solution {
//     fun getMinimumDifference(root: TreeNode?): Int {
//         var prev: Int? = null
//         var minDiff = Int.MAX_VALUE
//
//         fun inorderTraverse(node: TreeNode?) {
//             node ?: return  // More idiomatic than: if (node == null) return
//
//             inorderTraverse(node.left)
//
//             prev?.let {  // More idiomatic than: if (prev != null)
//                 minDiff = minOf(minDiff, node.`val` - it)  // 'it' refers to prev
//             }
//             prev = node.`val`
//
//             inorderTraverse(node.right)
//         }
//
//         inorderTraverse(root)
//         return minDiff
//     }
// }

/*
 * KOTLIN SYNTAX TIPS based on your original code:
 *
 * 1. NULL CHECKS with Elvis operator (?:) - NOT just for assignments!
 *
 *    Assignment usage (what you might know):
 *    val value = nullableValue ?: defaultValue
 *
 *    Control flow usage (expression statement):
 *    ❌ if (root == null) { return }
 *    ✅ root ?: return  (Elvis operator - more concise)
 *
 *    How it works:
 *    - If root is NOT null: expression evaluates to root (value ignored)
 *    - If root IS null: expression evaluates to 'return', which exits function
 *    - This is an "expression statement" - the expression is evaluated for its side effect
 *
 *    ❌ if (prev != null) { minDiff = minOf(minDiff, root.`val` - prev!!) }
 *    ✅ prev?.let { minDiff = minOf(minDiff, root.`val` - it) }
 *       (Safe call + let - avoids !! operator)
 *
 * 2. MIN FUNCTION:
 *    ❌ min(answer, sortedL[i + 1] - sortedL[i])
 *    ✅ minOf(answer, sortedL[i + 1] - sortedL[i])
 *       (min() is deprecated for two values, use minOf())
 *
 * 3. COLLECTION OPERATIONS:
 *    ❌ val l = set.toList()
 *        val sortedL = l.sorted()
 *    ✅ val sortedL = set.sorted()  (Direct chaining)
 *
 *    ❌ for (i in 0 until sortedL.size - 1) {
 *           answer = minOf(answer, sortedL[i + 1] - sortedL[i])
 *        }
 *    ✅ sortedL.zipWithNext().minOfOrNull { it.second - it.first } ?: Int.MAX_VALUE
 *       (More functional, handles empty case)
 *
 *    minOfOrNull vs minOf:
 *    - minOf(): Returns the minimum value, BUT throws exception if collection is EMPTY
 *    - minOfOrNull(): Returns the minimum value, OR returns NULL if collection is EMPTY
 *
 *    When does minOfOrNull return null?
 *    - When the collection/sequence is EMPTY (size = 0)
 *    - Example: emptyList<Int>().minOfOrNull { it } → returns null
 *    - Example: listOf(1, 2, 3).minOfOrNull { it } → returns 1
 *
 *    Why use it with zipWithNext()?
 *    - zipWithNext() creates pairs of consecutive elements
 *    - If list has < 2 elements, zipWithNext() returns empty list
 *    - So minOfOrNull returns null, then we use ?: Int.MAX_VALUE as fallback
 *
 * 4. SAFE CALL OPERATOR:
 *    ❌ if (root.left != null) { traverse(root.left) }
 *    ✅ root.left?.let { traverse(it) }
 *    Or even simpler: root.left?.let(::traverse)
 *
 * 5. VARIABLE NAMING:
 *    ❌ val l = set.toList()  (too short, unclear)
 *    ✅ val sortedValues = set.sorted()
 *
 * 6. IMMUTABILITY:
 *    Prefer 'val' over 'var' when possible
 *    ❌ var answer = Int.MAX_VALUE
 *    ✅ val answer = ... (if you can compute it directly)
 *
 * 7. FUNCTION REFERENCES:
 *    If function signature matches, you can use ::functionName
 *    root.left?.let(::traverse)  instead of root.left?.let { traverse(it) }
 *
 *
 * DETAILED ELVIS OPERATOR EXPLANATION:
 *
 * The Elvis operator (?:) is an EXPRESSION, not just for assignments!
 *
 * Basic syntax: leftExpression ?: rightExpression
 * - If leftExpression is NOT null: result is leftExpression
 * - If leftExpression IS null: result is rightExpression
 *
 * Examples:
 *
 * 1. Assignment (common use):
 *    val name = nullableName ?: "Unknown"
 *    // If nullableName is null, name = "Unknown", else name = nullableName
 *
 * 2. Expression statement (for control flow):
 *    root ?: return
 *    // If root is null, execute 'return' (exits function)
 *    // If root is not null, expression evaluates to root (but we don't use it)
 *
 * 3. With throw:
 *    val value = nullableValue ?: throw IllegalArgumentException("Value required")
 *
 * 4. With other expressions:
 *    val result = compute() ?: error("Computation failed")
 *
 * The key insight: In Kotlin, any expression can be used as a statement.
 * When you write "root ?: return", you're using the Elvis operator expression
 * as a statement - Kotlin evaluates it, and if root is null, it executes 'return'.
 */

// Your original approach refactored with better Kotlin syntax:
// class Solution {
//     fun getMinimumDifference(root: TreeNode?): Int {
//         val values = mutableSetOf<Int>()
//
//         fun traverse(node: TreeNode?) {
//             node ?: return  // Instead of: if (node == null) return
//
//             values.add(node.`val`)
//
//             // Instead of: if (root.left != null) { traverse(root.left) }
//             node.left?.let(::traverse)
//             node.right?.let(::traverse)
//         }
//
//         traverse(root)
//
//         // More idiomatic: use zipWithNext() for consecutive pairs
//         return values.sorted()
//             .zipWithNext()
//             .minOfOrNull { it.second - it.first }
//             ?: Int.MAX_VALUE
//     }
// }

/*
 * DETAILED EXPLANATION: minOfOrNull and when it returns null
 *
 * minOfOrNull returns null ONLY when the collection is EMPTY.
 *
 * Examples:
 *
 * 1. Empty collection:
 *    emptyList<Int>().minOfOrNull { it }           → null
 *    listOf<Int>().minOfOrNull { it }              → null
 *
 * 2. Non-empty collection:
 *    listOf(5, 2, 8).minOfOrNull { it }           → 2
 *    listOf(1).minOfOrNull { it }                  → 1
 *
 * 3. With zipWithNext() (creates pairs of consecutive elements):
 *    listOf(1, 2, 3).zipWithNext()                → [(1,2), (2,3)]
 *    listOf(1).zipWithNext()                       → [] (empty!)
 *    emptyList<Int>().zipWithNext()                → [] (empty!)
 *
 *    So in your code:
 *    values.sorted().zipWithNext().minOfOrNull { ... }
 *
 *    If values has < 2 elements:
 *    - zipWithNext() returns empty list
 *    - minOfOrNull returns null
 *    - Then ?: Int.MAX_VALUE provides fallback
 *
 * 4. Comparison with minOf (throws exception on empty):
 *    listOf(1, 2, 3).minOf { it }                 → 1 (works)
 *    emptyList<Int>().minOf { it }                → NoSuchElementException! (crashes)
 *
 *    That's why minOfOrNull is safer - it returns null instead of crashing.
 */
