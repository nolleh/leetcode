class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = cnt = 0
        for i in range(len(nums)):
            if nums[i] == val:
                cnt += 1
            else:
                # if not val, then put the value that current position
                nums[j] = nums[i]
                # mv to next ptr
                j += 1
        return len(nums) - cnt
