class Solution {
    fun snakesAndLadders(board: Array<IntArray>): Int {
        val n = board.size
        val target = n * n
        val queue = ArrayDeque<Pair<Int, Int>>()
        val visited = BooleanArray(target + 1)

        fun getPosition(square: Int): Pair<Int, Int> {
            val quot = (square - 1) / n
            val rem = (square - 1) % n
            val row = (n - 1) - quot

            val col = if (quot % 2 == 0) {
                rem
            } else {
                (n - 1) - rem
            }
            return Pair(row, col)
        }

        queue.add(Pair(1, 0))
        visited[1] = true

        while (queue.isNotEmpty()) {
            val (curr, moves) = queue.removeFirst()

            for (dice in 1..6) {
                var next = curr + dice
                if (next > target) continue  // check boundary

                // check (row, col)
                val (row, col) = getPosition(next)

                // if there is labber or snake
                if (board[row][col] != -1) {
                    next = board[row][col]
                }

                if (next == target) return moves + 1

                if (!visited[next]) {
                    visited[next] = true
                    queue.add(Pair(next, moves + 1))
                }
            }
        }
        return -1
    }
}

