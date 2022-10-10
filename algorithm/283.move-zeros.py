class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # in-place doesn't means that all extra space coulnd't be used. 
        # it means 'do not create extra whole list'
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
