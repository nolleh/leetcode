/**
 * 238. Product of Array Except Self
 * https://leetcode.com/problems/product-of-array-except-self/
 *
 * Difficulty: Medium
 *
 * Given an integer array nums, return an array answer such that answer[i]
 * is equal to the product of all the elements of nums except nums[i].
 *
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 * You must write an algorithm that runs in O(n) time and without using the division operation.
 *
 * Example 1:
 * Input: nums = [1,2,3,4]
 * Output: [24,12,8,6]
 *
 * Example 2:
 * Input: nums = [-1,1,0,-3,3]
 * Output: [0,0,9,0,0]
 *
 * Constraints:
 * - 2 <= nums.length <= 10^5
 * - -30 <= nums[i] <= 30
 *
 * Follow-up: Can you solve it in O(1) extra space? (output array doesn't count)
 */

class Solution {
    /**
     * Approach 1: Left and Right arrays
     * Time Complexity: O(?)
     * Space Complexity: O(?)
     */
    public int[] productExceptSelf(int[] nums) {
        // TODO: Implement using left and right arrays
        // Hint: left[i] = product of all elements to the left of i
        // Hint: right[i] = product of all elements to the right of i
        // Hint: answer[i] = left[i] * right[i]
        int[] left = new int[nums.length];
        int[] right = new int[nums.length];

        left[0] = 1;
        for (int i = 0; i < nums.length - 1; i++) {
            // Left[2] = left[1] * nums[1]
            left[i + 1] = left[i] * nums[i];
        }

        right[nums.length - 1] = 1;
        // right[2] = right[3] * nums[3]
        for (int i = nums.length - 2; i >= 0; i--) {
            right[i] = right[i + 1] * nums[i + 1];
        }

        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            result[i] = left[i] * right[i];
        }

        return result;
    }

    /**
     * Approach 2: Optimized - O(1) space
     * Time Complexity: O(?)
     * Space Complexity: O(?)
     */
    public int[] productExceptSelfOptimized(int[] nums) {
        // TODO: Implement without using extra arrays
        // Hint: Use result array to store left products first
        // Hint: Then multiply with right products using a variable

        int[] result = new int[nums.length];

        result[0] = 1;
        for (int i = 0; i < nums.length -1; i++) {
            result[i+1] = result[i] * nums[i];
        }

        int right = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            result[i] *= right;
            right *= nums[i];
        }

        return result;
    }
}

