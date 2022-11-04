class Solution:
    def rob(self, nums: List[int]) -> int:
        ## return maximum with not visiting adjacent houses.
        memo = {}
        def iter(i: int):
            if i in memo:
                return memo[i]
            if i <= 1:
                return nums[i]
            ans = 0
            for j in range(2, i + 1):
                ans = max(nums[i] + iter(i - j), ans)
                memo[i] = ans
            return ans

        output = 0 
        for i in range(len(nums)):
            output = max(iter(i), output)
        return output
