class Solution {
    fun canFinish(numCourses: Int, prerequisites: Array<IntArray>): Boolean {
        val graph = mutableMapOf<Int, MutableList<Int>>()

        for ((a, b) in prerequisites) {
            graph.getOrPut(a) { mutableListOf<Int>() }.add(b)
        }

        // 0: unvisit, 1: visiting, 2: visited
        val states = mutableMapOf<Int, Int>()
        fun hasCycle(i: Int): Boolean {
            if (states[i] == 1) return true
            if (states[i] == 2) return false

            states[i] = 1
            for (prereq in graph[i] ?: emptyList()) {
                if (hasCycle(prereq)) return true
            }
            states[i] = 2
            return false
        }

        for (i in 0 until numCourses) {
            if (hasCycle(i)) {
                return false
            }
        }
        return true
    }
}

