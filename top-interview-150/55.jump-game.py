class Solution:
    def canJump(self, nums: List[int]) -> bool:

        maxjump = 0
        for i, n in enumerate(nums):
            if maxjump < i:
                return False
            maxjump = max(maxjump,n + i)
        return True
