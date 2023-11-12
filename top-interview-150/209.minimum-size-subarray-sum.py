class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # subarray (consequence)
        # return minimal length of a subarray whose sum is greater than or equal

        global_min_cnt = sys.maxsize
        curr_cnt = 0

        # [2,3,1,2,4,3]
        # 2 -> 2 < target
        # 3 -> 2 + 3 < target, 3 < target
        # 1 -> 2 + 3 + 1 < target
        # 2 -> 2 + 3 + 1 + 2 >= target -> answer = 4, mv l p -> 3 + 1 + 2
        # 4 -> while 3 + 1 + 2 + 4 >= target -> mv lp -> 1 + 2 + 4, answercnt > count(1+2+4);

        l = 0
        curr_sum = 0
        for r in range(0, len(nums)):
            curr_sum += nums[r]
            curr_cnt += 1
            while curr_sum >= target:
                global_min_cnt = min(global_min_cnt, curr_cnt)
                curr_sum -= nums[l]
                curr_cnt -= 1
                l += 1

        return global_min_cnt if global_min_cnt != sys.maxsize else 0
