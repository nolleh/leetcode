class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # at least three elements. and if the difference between any two consecutive elements is the same
        # ex. [1,3,5,7,9] (diff 2), [7,7,7,7] (diff 0), [3,-1,-5,-9] (diff: -2)

        # given an integer array `nums`, return the arithmatic subarrays
        # subarray: consecutive?

        memo = {}

        is_arithmetic = lambda i: nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]

        def dp(i):
            # input : ending index i of subarray
            # output: count of arithmetic subarray ending at i

            ## Base case
            if i < 2:
                # No chance to make arithmetic subarray less than 3 elements
                return 0
            elif i == 2:
                memo[i] = int(is_arithmetic(i))
                return memo[i]

            ## General cases
            prev_count = dp(i - 1)
            if is_arithmetic(i):
                # arithmetric subarray can extend from previous index to current index
                memo[i] = prev_count + 1
                return memo[i]
            else:
                # arithmetric subarray cannot extend from previous index to current index
                memo[i] = 0
                return memo[i]

        dp(len(nums) - 1)
        return sum(memo.values())
