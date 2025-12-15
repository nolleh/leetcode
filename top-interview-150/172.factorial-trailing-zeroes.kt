/**
 * Problem: 172. Factorial Trailing Zeroes
 * Link: https://leetcode.com/problems/factorial-trailing-zeroes/
 *
 * Approach: Count factors of 5
 * - Trailing zeros come from factors of 10 (2 × 5)
 * - In n!, there are always more 2s than 5s
 * - So we only need to count factors of 5
 * - Count: n/5 + n/25 + n/125 + ...
 *
 * Time Complexity: O(log n) - we divide n by 5 repeatedly
 * Space Complexity: O(1)
 */

class Solution {
    fun trailingZeroes(n: Int): Int {
        var count = 0
        var divisor = 5

        // Count factors of 5, 25, 125, ...
        // We need to be careful with overflow, so we check n/divisor instead of divisor <= n
        while (n / divisor > 0) {
            count += n / divisor

            // Check if divisor * 5 would overflow
            if (divisor > Int.MAX_VALUE / 5) {
                break
            }
            divisor *= 5
        }

        return count
    }
}

// Alternative approach: using repeated division
class Solution2 {
    fun trailingZeroes(n: Int): Int {
        var count = 0
        var num = n

        // 100/5 = 20 -> 5's multiplier = 20
        // 20/5 = 4 -> 25's multiplier = 4
        while (num > 0) {
            num /= 5
            count += num
        }

        return count
    }
}

fun main() {
    val sol = Solution()

    // Test cases
    println(sol.trailingZeroes(3))   // Expected: 0 (3! = 6)
    println(sol.trailingZeroes(5))   // Expected: 1 (5! = 120)
    println(sol.trailingZeroes(10))  // Expected: 2 (10! = 3628800)
    println(sol.trailingZeroes(25))  // Expected: 6
    println(sol.trailingZeroes(100)) // Expected: 24

    println("\n--- Solution2 ---")
    val sol2 = Solution2()
    println(sol2.trailingZeroes(3))   // Expected: 0
    println(sol2.trailingZeroes(5))   // Expected: 1
    println(sol2.trailingZeroes(10))  // Expected: 2
    println(sol2.trailingZeroes(25))  // Expected: 6
    println(sol2.trailingZeroes(100)) // Expected: 24
}
