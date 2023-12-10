class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        cnt = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] in s:
                cnt += 1
            else:
                nums[j] = nums[i]
                s.add(nums[j])
                j += 1
        return len(nums) - cnt
