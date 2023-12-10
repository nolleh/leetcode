from collections import defaultdict


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # at most twice
        d = defaultdict(int)
        cnt = 0
        j = 0

        for i in range(len(nums)):
            if nums[i] in d and d[nums[i]] > 1:
                cnt += 1
            else:
                nums[j] = nums[i]
                d[nums[i]] += 1
                j += 1
        return len(nums) - cnt
