from typing import List

# EASY
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # runningSum[i] = sum(nums[0]...nums[i])
        # return running sum of nums;

        # space complexity 1+2+3+4..n O(N)
        # time complexity O(N)
        # res = []

        # for i, n in enumerate(nums):
        #  res.append(sum(nums[:i+1]))
        # return res

        # list comprehension
        return [sum(nums[: i + 1]) for i in range(len(nums))]
