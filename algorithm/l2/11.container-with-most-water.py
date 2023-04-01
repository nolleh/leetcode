class Solution:
    def maxArea(self, height: List[int]) -> int:
        # area formed between the lines will always be limited by the height of the shorter line.
        # farther the lines, the more will be the area obtained.

        l = 0
        r = len(height) - 1
        maxarea = 0
        while l < r:
            width = r - l
            maxarea = max(maxarea, min(height[l], height[r]) * width)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxarea
