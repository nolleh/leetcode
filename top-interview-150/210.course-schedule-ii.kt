class Solution {
    fun findOrder(numCourses: Int, prerequisites: Array<IntArray>): IntArray {
        val graph = mutableMapOf<Int, MutableList<Int>>()
        for (p in prerequisites) {
            graph.getOrPut(p[0]) { mutableListOf<Int>() }.add(p[1])
        }

        val visit = mutableMapOf<Int, Int>()
        val result = mutableListOf<Int>()

        fun hasCycle(current: Int): Boolean {
            if (visit[current] == 1) return true
            if (visit[current] == 2) return false

            visit[current] = 1

            for (preq in graph[current] ?: emptyList()) {
                if (hasCycle(preq)) return true
            }

            visit[current] = 2
            result.add(current)
            return false
        }

        for (i in 0 until numCourses) {
            if (hasCycle(i)) return intArrayOf()
        }

        return result.toIntArray()
    }
}

