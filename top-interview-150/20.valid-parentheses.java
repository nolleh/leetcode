import java.util.Stack;
import java.util.HashMap;
import java.util.Map;

/**
 * 20. Valid Parentheses
 * https://leetcode.com/problems/valid-parentheses/
 *
 * Difficulty: Easy
 *
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 * determine if the input string is valid.
 *
 * An input string is valid if:
 * 1. Open brackets must be closed by the same type of brackets.
 * 2. Open brackets must be closed in the correct order.
 * 3. Every close bracket has a corresponding open bracket of the same type.
 *
 * Example 1:
 * Input: s = "()"
 * Output: true
 *
 * Example 2:
 * Input: s = "()[]{}"
 * Output: true
 *
 * Example 3:
 * Input: s = "(]"
 * Output: false
 *
 * Example 4:
 * Input: s = "([])"
 * Output: true
 *
 * Constraints:
 * - 1 <= s.length <= 10^4
 * - s consists of parentheses only '()[]{}'
 *
 * Pattern: Stack
 * Time Complexity: O(?)
 * Space Complexity: O(?)
 */

class Solution {
    /**
     * Approach: Stack with HashMap for matching
     *
     * Key insights:
     * 1. Use Stack to track opening brackets
     * 2. When closing bracket found: check if it matches top of stack
     * 3. At the end, stack should be empty
     */
    public boolean isValid(String s) {
        // TODO: Implement stack-based solution
        // Hint: Use Stack<Character> to store opening brackets
        // Hint: Use HashMap to map opening → closing brackets
        // Hint: For closing bracket: check if stack top matches

        Map<Character, Character> map = new HashMap<>();
        map.put('(', ')');
        map.put('[', ']');
        map.put('{', '}');

        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (map.containsKey(c)) {
                stack.push(c);
            } else {
                if (stack.isEmpty() || map.get(stack.pop()) != c) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}

