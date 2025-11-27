class Solution {
    // Method 1: Two Pointer (Recommended)
    // Time: O(n), Space: O(1)
    fun twoSum(numbers: IntArray, target: Int): IntArray {
        var left = 0
        var right = numbers.size - 1

        while (left < right) {
            val sum = numbers[left] + numbers[right]
            when {
                sum == target -> return intArrayOf(left + 1, right + 1)
                sum < target -> left++
                else -> right--
            }
        }
        return intArrayOf(-1, -1)
    }

    // Method 2: Binary Search
    // Time: O(n log n), Space: O(1)
    fun twoSumBinarySearch(numbers: IntArray, target: Int): IntArray {
        for (i in numbers.indices) {
            val complement = target - numbers[i]
            val index = binarySearch(numbers, complement, i + 1)
            if (index != -1) {
                return intArrayOf(i + 1, index + 1)
            }
        }
        return intArrayOf(-1, -1)
    }

    private fun binarySearch(numbers: IntArray, target: Int, start: Int): Int {
        var left = start
        var right = numbers.size - 1

        while (left <= right) {
            val mid = left + (right - left) / 2
            when {
                numbers[mid] == target -> return mid
                numbers[mid] < target -> left = mid + 1
                else -> right = mid - 1
            }
        }
        return -1
    }
}
