class Solution {
    fun numIslands(grid: Array<CharArray>): Int {
        var count = 0
        fun dfs(r: Int, c: Int) {
            if (r < 0 || c < 0 || r >= grid.size || c >= grid[0].size) return
            if (grid[r][c] == '0') return

            grid[r][c] = '0'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        }

        for (r in grid.indices) {
            for (c in grid[r].indices) {
                if (grid[r][c] == '1') {
                    dfs(r, c)
                    count++
                }
            }
        }
        return count
    }

    fun numIslandsBfs(grid: Array<CharArray>): Int {
        // store the position of the island
        val q = ArrayDeque<Pair<Int, Int>>()
        var count = 0

        for (r in grid.indices) {
            for (c in grid[r].indices) {
                if (grid[r][c] == '1') {
                    q.add(Pair(r, c))

                    while (q.isNotEmpty()) {
                        val (r, c) = q.removeFirst()
                        if (r < 0 || c < 0 || r >= grid.size || c >= grid[0].size) continue
                        if (grid[r][c] == '0') continue

                        grid[r][c] = '0'
                        q.add(Pair(r - 1, c))
                        q.add(Pair(r + 1, c))
                        q.add(Pair(r, c - 1))
                        q.add(Pair(r, c + 1))
                    }
                    count++
                }
            }
        }

        return count
    }
}

