import java.util.HashMap;
import java.util.Map;

/**
 * 3. Longest Substring Without Repeating Characters
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 *
 * Difficulty: Medium
 *
 * Given a string s, find the length of the longest substring without repeating characters.
 *
 * Example 1:
 * Input: s = "abcabcbb"
 * Output: 3
 * Explanation: The answer is "abc", with the length of 3.
 *
 * Example 2:
 * Input: s = "bbbbb"
 * Output: 1
 * Explanation: The answer is "b", with the length of 1.
 *
 * Example 3:
 * Input: s = "pwwkew"
 * Output: 3
 * Explanation: The answer is "wke", with the length of 3.
 *
 * Constraints:
 * - 0 <= s.length <= 5 * 10^4
 * - s consists of English letters, digits, symbols and spaces.
 *
 * Pattern: Sliding Window
 * Time Complexity: O(?)
 * Space Complexity: O(?)
 */

class Solution {
    /**
     * Approach: Sliding Window with HashMap
     *
     * Key insights:
     * 1. Use HashMap to store character → last seen index
     * 2. Window = [start, i] where i is current position
     * 3. When duplicate found: move start to (duplicate's index + 1)
     * 4. But ensure start never moves backward!
     */
    public int lengthOfLongestSubstring(String s) {
        // TODO: Implement sliding window solution
        // Hint: Use HashMap<Character, Integer> to store char → index
        // Hint: Track window start position
        // Hint: Track maximum length seen so far

        int l = 0;
        int r = 0;
        int maxLength = 0;
        Map<Character, Integer> map = new HashMap<>();

        while (r < s.length()) {
            if (map.containsKey(s.charAt(r))) {
                l = Math.max(l, map.get(s.charAt(r)) + 1);
            }
            map.put(s.charAt(r), r);
            maxLength = Math.max(maxLength, r - l + 1);
            r++;
        }
        return maxLength;
    }
}
