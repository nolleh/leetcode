class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prefix_i = len(nums) - k % len(nums)
        prefix = nums[prefix_i:]
        r = len(nums) -1
        for i in range(prefix_i -1, -1, -1):
            nums[r] = nums[i]
            r-=1
        for i in range(len(prefix)):
            nums[i] = prefix[i]
