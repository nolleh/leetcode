class Solution {
    // Better Approach: Check if current value < next value
    // Time: O(n), Space: O(1)
    fun romanToInt(s: String): Int {
        val values = mapOf(
            'I' to 1,
            'V' to 5,
            'X' to 10,
            'L' to 50,
            'C' to 100,
            'D' to 500,
            'M' to 1000
        )

        var result = 0

        for (i in s.indices) {
            val currentValue = values[s[i]]!!

            // If current value < next value, subtract; otherwise, add
            if (i < s.length - 1 && currentValue < values[s[i + 1]]!!) {
                result -= currentValue
            } else {
                result += currentValue
            }
        }

        return result
    }
}

