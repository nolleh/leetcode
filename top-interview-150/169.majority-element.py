from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #     cnter = Counter(nums)
        #     for k,v in cnter.items():
        #         if v > len(nums)/2:
        #             return k
        #     return -1
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
