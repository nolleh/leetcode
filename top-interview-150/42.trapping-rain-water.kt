class Solution {
    fun trap(height: IntArray): Int {
        var left = 0
        var right = height.size - 1
        var answer = 0

        var leftMax = 0
        var rightMax = 0

        while (left <= right) {
            if (leftMax < rightMax) {
                leftMax = maxOf(leftMax, height[left])
                answer += leftMax - height[left]
                left++

            } else {
                rightMax = maxOf(rightMax, height[right])
                answer += rightMax - height[right]
                right--
            }
        }
        return answer
    }
}

