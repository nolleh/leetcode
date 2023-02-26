class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # given numbers
        # count all means that evaluated to target by placing operator (+, or - ) for numbers.
        # for ex. [1,1,1,1,1]  target = 3
        # -1 + 1 + 1 + 1 + 1 = 3
        # +1 - 1 + 1 + 1 + 1 = 3
        # ...
        # +1 + 1 + 1 + 1 - 1 = 3
        # answer is 5.

        memo = defaultdict(int)

        def dfs(pos: int, target: int) -> int:
            key = (pos, target)
            if key in memo:
                return memo[key]

            if pos == len(nums):
                return 1 if target == 0 else 0
            memo[key] = dfs(pos + 1, target + nums[pos]) + dfs(
                pos + 1, target - nums[pos]
            )
            return memo[key]

        return dfs(0, target)
