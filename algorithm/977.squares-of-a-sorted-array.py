class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0, len(nums) -1
        res = []
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res = [nums[l] * nums[l]] + res
                l += 1
            else:
                res = [nums[r] * nums[r]] + res
                r -= 1
        return res
