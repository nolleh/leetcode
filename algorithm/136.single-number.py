class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # every elemnt appears twice expect for one.
        # must implement with a linear complexity and use only constant extraspace.
        # TC O(N)
        # SC O(1)

        ## 01 xor 01 xor 10 = 10
        output = nums[0]
        for n in nums[1:]:
            output ^= n 
        return output
