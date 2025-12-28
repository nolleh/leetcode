class Solution {
    fun threeSum(nums: IntArray): List<List<Int>> {
        // Key insight: Reduce 3Sum to 2Sum by fixing one element
        // Two pointers ONLY works on sorted arrays
        nums.sort()

        val result = mutableListOf<List<Int>>()
        for (i in nums.indices) {
            // Skip duplicate values for the fixed element to avoid duplicate triplets
            // Must check i > 0 to avoid out of bounds
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue
            }

            var target = -nums[i]
            var l = i + 1
            var r = nums.size - 1

            while (l < r) {

                if (nums[l] + nums[r] == target) {
                    result.add(listOf(nums[i], nums[l], nums[r]))
                    l++
                    r--
                    // Skip duplicates AFTER finding answer (safer approach)
                    // At this point, l-1 and r+1 are guaranteed to be valid indices
                    // This prevents duplicate triplets like [-1,0,1] appearing twice
                    while (l < r && nums[l] == nums[l - 1]) l++
                    while (l < r && nums[r] == nums[r + 1]) r--
                } else if (nums[l] + nums[r] < target) {
                    l++
                } else {
                    r--
                }
            }
        }
        return result
    }
}

