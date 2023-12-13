class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = len(nums) - k % len(nums)
        first = nums[k:]
        r = len(nums) - 1
        for i in range(k - 1, -1, -1):
            nums[r] = nums[i]
            r -= 1
        for i in range(len(first)):
            nums[i] = first[i]
