class Solution {
    fun removeElement(nums: IntArray, `val`: Int): Int {
        // Two Pointer approach: O(n) time, O(1) space
        var k = 0  // k equals the count of non-val values stored

        for (i in nums.indices) {
            if (nums[i] != `val`) {
                nums[k] = nums[i]
                k++
            }
        }

        return k
    }
}
