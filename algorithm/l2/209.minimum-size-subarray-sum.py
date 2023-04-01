class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # minimal length of a subarray whose sum is greater than or equal to 'target'
        # 'SUBARRAY' contagious.
        n = len(nums)
        ans = sys.maxsize
        l = 0
        sum = 0

        for i in range(n):
            sum += nums[i]
            while sum >= target:
                ans = min(ans, i + 1 - l)
                sum -= nums[l]
                l += 1
        return ans if ans != sys.maxsize else 0
