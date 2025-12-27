class Solution {
    fun calcEquation(equations: List<List<String>>, values: DoubleArray, queries: List<List<String>>): DoubleArray {
        // Build graph: variable -> list of (neighbor, weight)
        // a / b = 2 means: a -> b with weight 2.0, b -> a with weight 0.5
        val graph = mutableMapOf<String, MutableList<Pair<String, Double>>>()

        for (i in equations.indices) {
            val a = equations[i][0]
            val b = equations[i][1]
            val value = values[i]

            graph.getOrPut(a) { mutableListOf() }.add(Pair(b, value))
            graph.getOrPut(b) { mutableListOf() }.add(Pair(a, 1.0 / value))
        }

        // Process each query
        val result = DoubleArray(queries.size)
        for (i in queries.indices) {
            val start = queries[i][0]
            val end = queries[i][1]

            // If either variable doesn't exist in graph
            if (!graph.containsKey(start) || !graph.containsKey(end)) {
                result[i] = -1.0
                continue
            }

            // Same variable
            if (start == end) {
                result[i] = 1.0
                continue
            }

            // DFS to find path from start to end
            val visited = mutableSetOf<String>()
            result[i] = dfs(graph, start, end, visited)
        }

        return result
    }

    private fun dfs(
        graph: Map<String, List<Pair<String, Double>>>,
        current: String,
        target: String,
        visited: MutableSet<String>
    ): Double {
        // Mark as visited
        visited.add(current)

        // Check all neighbors
        // a / c -> a -> b(x2) -> c (x3)
        for ((neighbor, weight) in graph[current] ?: emptyList()) {
            if (neighbor == target) {
                return weight
            }

            if (neighbor !in visited) {
                val result = dfs(graph, neighbor, target, visited)
                if (result != -1.0) {
                    return weight * result
                }
            }
        }

        // No path found
        return -1.0
    }
}

