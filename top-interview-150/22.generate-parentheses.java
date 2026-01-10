import java.util.ArrayList;
import java.util.List;

/**
 * 22. Generate Parentheses
 * https://leetcode.com/problems/generate-parentheses/
 *
 * Difficulty: Medium
 *
 * Given n pairs of parentheses, write a function to generate all combinations
 * of well-formed parentheses.
 *
 * Example 1:
 * Input: n = 3
 * Output: ["((()))","(()())","(())()","()(())","()()()"]
 *
 * Example 2:
 * Input: n = 1
 * Output: ["()"]
 *
 * Constraints:
 * - 1 <= n <= 8
 *
 * Pattern: Backtracking with Pruning
 * Time Complexity: O(?)
 * Space Complexity: O(?)
 */

class Solution {
    /**
     * Approach: Backtracking with constraints
     *
     * Key insights:
     * 1. Track number of open '(' and close ')' brackets used
     * 2. Can add '(' if open < n
     * 3. Can add ')' if close < open (ensures validity!)
     * 4. Base case: when length == 2*n, add to result
     *
     * This is more efficient than generating all permutations and filtering,
     * because we prune invalid branches early (close >= open would be invalid).
     */
    public List<String> generateParenthesis(int n) {
        // TODO: Implement backtracking solution
        // Hint: Track current string (or StringBuilder), open count, close count
        // Hint: Use helper method: backtrack(current, open, close, n, result)
        // Hint: Add '(' if open < n
        // Hint: Add ')' if close < open

        List<String> result = new ArrayList<>();
        backtrack(new StringBuilder(), 0, 0, n, result);
        return result;
    }

    // TODO: Add backtracking helper method
    private void backtrack(StringBuilder curr, int open, int close, int n, List<String> result) {
        // Base case: current length == 2*n
        // Try adding '(' if open < n
        // Try adding ')' if close < open
        if (curr.length() == 2 * n) {
            result.add(curr.toString());
            return;
        }

        if (open < n) {
            curr.append('(');
            backtrack(curr, open + 1, close, n, result);
            curr.deleteCharAt(curr.length() - 1);
        }

        if (close < open) {
            curr.append(')');
            backtrack(curr, open, close + 1, n, result);
            curr.deleteCharAt(curr.length() - 1);
        }

    }
}

