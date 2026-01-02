import java.util.LinkedList;
import java.util.Queue;

/**
 * 200. Number of Islands
 * https://leetcode.com/problems/number-of-islands/
 *
 * Difficulty: Medium
 *
 * Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
 * return the number of islands.
 *
 * An island is surrounded by water and is formed by connecting adjacent lands
 * horizontally or vertically. You may assume all four edges of the grid are surrounded by water.
 *
 * Example 1:
 * Input: grid = [
 *   ["1","1","1","1","0"],
 *   ["1","1","0","1","0"],
 *   ["1","1","0","0","0"],
 *   ["0","0","0","0","0"]
 * ]
 * Output: 1
 *
 * Example 2:
 * Input: grid = [
 *   ["1","1","0","0","0"],
 *   ["1","1","0","0","0"],
 *   ["0","0","1","0","0"],
 *   ["0","0","0","1","1"]
 * ]
 * Output: 3
 *
 * Constraints:
 * - m == grid.length
 * - n == grid[i].length
 * - 1 <= m, n <= 300
 * - grid[i][j] is '0' or '1'
 */

class Solution {
    /**
     * Approach 1: DFS (Depth-First Search)
     * Time Complexity: O(?)
     * Space Complexity: O(?)
     */
    public int numIslands(char[][] grid) {
        // TODO: Implement DFS solution
        // Hint: When you find a '1', increment count and mark all connected lands as '0'
        // Hint: Use a helper DFS function to explore 4 directions

        int count = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[r].length; c++) {
                if (grid[r][c] == '1') {
                    dfs(grid, r, c);
                    count++;
                }
            }
        }

        return count;

    }

        private void dfs(char[][] grid, int r, int c) {
            if (r < 0 || c < 0 || r >= grid.length || c >= grid[0].length) {
                return;
            }
            if (grid[r][c] == '0') {
                return;
            }

            grid[r][c] = '0';
            dfs(grid, r-1, c);
            dfs(grid, r+1, c);
            dfs(grid, r, c-1);
            dfs(grid, r, c+1);
        }

    // TODO: Implement DFS helper method
    // private void dfs(char[][] grid, int r, int c) {
    //     // Check boundaries and if current cell is water
    //     // Mark as visited by changing '1' to '0'
    //     // Recursively explore 4 directions (up, down, left, right)
    // }

    /**
     * Approach 2: BFS (Breadth-First Search)
     * Time Complexity: O(?)
     * Space Complexity: O(?)
     */
    public int numIslandsBfs(char[][] grid) {
        // TODO: Implement BFS solution
        // Hint: Use a Queue to store coordinates
        // Hint: Process all connected lands level by level

        int count = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[r].length; c++) {
                if (grid[r][c] == '1') {
                    bfs(grid, r, c);
                    count++;
                }
            }
        }
        return count;
    }
    private void bfs(char[][] grid, int r, int c) {
            Queue<int[]> queue = new LinkedList<>();
            queue.add(new int[] {r, c});
            while (!queue.isEmpty()) {
                int[] curr = queue.poll();
                int currR = curr[0];
                int currC = curr[1];
                if (currR < 0 || currC < 0 || currR >= grid.length || currC >= grid[0].length) {
                    continue;
                }
                if (grid[currR][currC] == '0') {
                    continue;
                }
                grid[currR][currC] = '0';
                queue.add(new int[] {currR-1, currC});
                queue.add(new int[] {currR+1, currC});
                queue.add(new int[] {currR, currC-1});
                queue.add(new int[] {currR, currC+1});
            }
    }

}

