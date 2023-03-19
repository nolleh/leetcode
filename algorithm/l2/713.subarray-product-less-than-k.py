class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than 'k'
        first = 0
        second = 0
        product = 1
        combos = 0

        for second in range(len(nums)):
            # add second to product
            product *= nums[second]
            # move first, till product is less than k
            while product >= k and first <= second:
                product /= nums[first]
                first += 1
            # count combos. Note that first is one place beyond the starting range, so add +1
            # if product *= nums[second] is less than k, then all sub array contributed to answer.
            combos += second - first + 1

        return combos
