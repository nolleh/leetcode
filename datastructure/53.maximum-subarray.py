from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # get max! - O(n)
        max_sub = nums[0]
        prv = nums[0]
        for n in nums[1:]:
            current = max(prv + n, n)
            max_sub = max(max_sub, current)
            prv = current
        return max_sub
