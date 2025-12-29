class Solution {
    fun setZeroes(matrix: Array<IntArray>): Unit {
        // Space: O(1) - only 2 boolean variables
        // Time: O(m*n) - 3 passes over matrix

        // Key Insight: Use first row and first column as markers
        // - matrix[0][j] = 0 means "column j should be zeroed"
        // - matrix[i][0] = 0 means "row i should be zeroed"

        var firstRowHasZero = false
        var firstColHasZero = false

        // PASS 1: Check if first row/col originally has zero
        // Why? Because we'll use them as markers, we need to remember their original state
        for (i in matrix.indices) {
            if (matrix[i][0] == 0) {
                firstColHasZero = true
            }
        }
        for (j in matrix[0].indices) {
            if (matrix[0][j] == 0) {
                firstRowHasZero = true
            }
        }

        // PASS 2: Mark first row/col when finding zeros in inner matrix
        // Start from index 1 to avoid overwriting markers
        for (i in 1 until matrix.size) {
            for (j in 1 until matrix[i].size) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0  // Mark: "row i has zero"
                    matrix[0][j] = 0  // Mark: "col j has zero"
                }
            }
        }

        // PASS 3a: Update inner matrix FIRST (crucial order!)
        // Why first? To preserve markers in row 0 and col 0
        // If we update row 0 first, we'd overwrite our markers!
        for (i in 1 until matrix.size) {
            for (j in 1 until matrix[i].size) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0
            }
        }

        // PASS 3b: Update first row LAST (after using markers)
        if (firstRowHasZero) {
            for (j in matrix[0].indices) {
                matrix[0][j] = 0
            }
        }

        // PASS 3c: Update first col LAST (after using markers)
        if (firstColHasZero) {
            for (i in matrix.indices) {
                matrix[i][0] = 0
            }
        }
    }
}

