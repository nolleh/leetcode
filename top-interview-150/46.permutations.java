import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import java.util.stream.Collectors;
/**
 * 46. Permutations
 * https://leetcode.com/problems/permutations/
 *
 * Difficulty: Medium
 *
 * Given an array nums of distinct integers, return all the possible permutations.
 * You can return the answer in any order.
 *
 * Example 1:
 * Input: nums = [1,2,3]
 * Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 *
 * Example 2:
 * Input: nums = [0,1]
 * Output: [[0,1],[1,0]]
 *
 * Example 3:
 * Input: nums = [1]
 * Output: [[1]]
 *
 * Constraints:
 * - 1 <= nums.length <= 6
 * - -10 <= nums[i] <= 10
 * - All the integers of nums are unique.
 *
 * Pattern: Backtracking
 * Time Complexity: O(?)
 * Space Complexity: O(?)
 */

class Solution {
    /**
     * Approach: Backtracking
     *
     * Key insights:
     * 1. Build permutations incrementally
     * 2. At each step, try adding each remaining number
     * 3. Backtrack by removing the last added number
     * 4. Base case: when no numbers remain, add current permutation to result
     */
    public List<List<Integer>> permute(int[] nums) {
        // TODO: Implement backtracking solution
        // Hint: Use List<List<Integer>> for result
        // Hint: Use helper method: backtrack(current, remaining)
        // Hint: Make a copy when adding to result (curr[:] in Python)
        List<List<Integer>> result = new ArrayList<>();
        // stream<int> -> stream<Integer> -> List<Integer>
        List<Integer> list = Arrays.stream(nums).boxed().collect(Collectors.toList());
        backtrack(new ArrayList<>(), list, result);
        return result;
    }

    private void backtrack(List<Integer> curr, List<Integer> remains, List<List<Integer>> result) {
        // Base case: if no elements remain, add current permutation
        // Recursive case: try adding each remaining element

        if (remains.isEmpty()) {
            result.add(new ArrayList<>(curr));
            return;
        }

        for (int i = 0; i < remains.size(); i++) {
            curr.add(remains.get(i));

            List<Integer> newRemains = new ArrayList<>(remains);
            newRemains.remove(i);

            backtrack(curr, newRemains, result);
            curr.remove(curr.size() - 1);
        }

    }
}

