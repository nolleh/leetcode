class Solution {
    fun spiralOrder(matrix: Array<IntArray>): List<Int> {
        val m = matrix.size
        val n = matrix[0].size
        val result = mutableListOf<Int>()

        var top = 0
        var bottom = m - 1
        var left = 0
        var right = n - 1

        while (top <= bottom && left <= right) {
            // Move right: top row from left to right
            for (j in left..right) {
                result.add(matrix[top][j])
            }
            top++

            // Move down: right column from top to bottom
            for (i in top..bottom) {
                result.add(matrix[i][right])
            }
            right--

            // Move left: bottom row from right to left (if still valid)
            if (top <= bottom) {
                for (j in right downTo left) {
                    result.add(matrix[bottom][j])
                }
                bottom--
            }

            // Move up: left column from bottom to top (if still valid)
            if (left <= right) {
                for (i in bottom downTo top) {
                    result.add(matrix[i][left])
                }
                left++
            }
        }

        return result
    }
}

