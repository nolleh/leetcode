/**
 * 70. Climbing Stairs
 * https://leetcode.com/problems/climbing-stairs/
 *
 * Difficulty: Easy
 *
 * You are climbing a staircase. It takes n steps to reach the top.
 * Each time you can either climb 1 or 2 steps.
 * In how many distinct ways can you climb to the top?
 *
 * Example 1:
 * Input: n = 2
 * Output: 2
 * Explanation: There are two ways to climb to the top.
 * 1. 1 step + 1 step
 * 2. 2 steps
 *
 * Example 2:
 * Input: n = 3
 * Output: 3
 * Explanation: There are three ways to climb to the top.
 * 1. 1 step + 1 step + 1 step
 * 2. 1 step + 2 steps
 * 3. 2 steps + 1 step
 *
 * Constraints:
 * - 1 <= n <= 45
 *
 * Pattern: Dynamic Programming (Fibonacci)
 */

class Solution {
    /**
     * Approach 1: Recursion with Memoization (Top-Down DP)
     * Time Complexity: O(?)
     * Space Complexity: O(?)
     */
    public int climbStairs(int n) {
        // TODO: Implement recursive solution with memoization
        // Hint: f(n) = f(n-1) + f(n-2)
        // Hint: Base cases: f(1) = 1, f(2) = 2
        // Hint: Use array or HashMap to cache results

        int[] memo = new int[n + 1];
        return helper(n, memo);
    }

    private int helper(int n, int[] memo) {
        if (n <= 2) return n;
        if (memo[n] != 0) return memo[n];
        memo[n] = helper(n - 1, memo) + helper(n - 2, memo);
        return memo[n];
    }

    /**
     * Approach 2: Iterative DP (Bottom-Up)
     * Time Complexity: O(?)
     * Space Complexity: O(?)
     */
    public int climbStairsIterative(int n) {
        // TODO: Implement iterative solution
        // Hint: Build up from f(1), f(2), ..., f(n)
        // Hint: Only need to track last 2 values

        int[] dp = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            if (i <= 2) {
                dp[i] = i;
                continue;
            }
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }

    /**
     * Approach 3: Space Optimized (Two Variables)
     * Time Complexity: O(?)
     * Space Complexity: O(?)
     */
    public int climbStairsOptimized(int n) {
        // TODO: Implement space-optimized solution
        // Hint: Only keep track of previous 2 values
        // Hint: No array needed!
        if (n <= 2) return n;

        int prev1 = 1;
        int prev2 = 2;
        for (int i = 3; i <= n; i++) {
            int current = prev1 + prev2;
            prev1 = prev2;
            prev2 = current;
        }
        return prev2;

    }
}

