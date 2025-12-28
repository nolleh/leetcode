class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        val left = IntArray(nums.size)
        val right = IntArray(nums.size)

        left[0] = 1
        right[nums.size - 1] = 1

        // [1, 2, 3, 4]
        // right[3] = 1
        // right[2] = 1 * 4 (right[3] * nums[3])
        val result = IntArray(nums.size)
        for (i in 0 until nums.size - 1) {
            left[i+1] = left[i] * nums[i]
        }
        for (i in nums.size - 2 downTo 0) {
            right[i] = right[i+1] * nums[i+1]
        }

        for (i in nums.indices) {
            result[i] = left[i] * right[i]
        }

        return result
    }

    // Optimized solution: O(1) extra space (output array doesn't count)
    fun productExceptSelfOptimized(nums: IntArray): IntArray {
        val result = IntArray(nums.size)
        result[0] = 1
        // result[1] = result[0] * nums[0]
        for (i in 1 until nums.size) {
            result[i] = result[i-1] * nums[i-1]
        }
        var right = 1
        for (i in nums.size - 1 downTo 0) {
            // result[2] = right(1) * nums[2] = 1 * 3 = 3
            // result[1] = right(3) * nums[1] = 3 * 2 = 6
            // result[0] = right(6) * nums[0] = 6 * 1 = 6
            result[i] *= right
            right *= nums[i]
        }

        return result
    }
}

