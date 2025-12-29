class Solution {
    fun maxArea(height: IntArray): Int {
        var left = 0
        var right = height.size - 1
        var answer = 0

        while (left < right) {
            val area = minOf(height[left], height[right]) * (right - left)
            answer = maxOf(answer, area)

            // Core insight: move the pointer with smaller height
            // Why? The shorter bar limits the area. Moving the taller bar
            // will only decrease width without possibility of increasing area.
            // Moving the shorter bar gives us a chance to find a taller bar.
            if (height[left] < height[right]) {
                left++
            } else {
                right--
            }
        }

        return answer
    }
}

