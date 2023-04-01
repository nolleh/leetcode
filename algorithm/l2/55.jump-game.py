class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        O(n) O(1)
        """
        max_pos = 0
        for curr_pos, max_jump in enumerate(nums):
            if max_pos < curr_pos:
                return False
            if max_pos < curr_pos + max_jump:
                max_pos = curr_pos + max_jump
        return True
