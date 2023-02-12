class Solution:
    nums = []

    def climbStairs(self, n: int) -> int:
        if len(self.nums) == 0:
            self.nums = [0] * n
        # 1 or 2 step
        # 1. former answer plus 1 to as prefix, postfix

        # 1, 2, 3, 5, 8

        # n = 4
        # plus 1 to former.
        # 1 + 1 + 1 + 1
        # 1 + 2 + 1
        # 2 + 1 + 1
        # and add 2 when evennumb
        # 1 + 1 + 2
        # 2 + 2

        # c5 = 8
        # 1 + 1 + 1 + 1 + 1
        # 1 + 2 + 1 + 1
        # 2 + 1 + 1 + 1
        # 1 + 1 + 2 + 1
        # 2 + 2 + 1
        ## and add ..
        # 1 + 1 + 1 + 2 # for c3 + 2
        # 2 + 1 + 2 # c3 + 2
        # 1 + 2 + 2 # c3 + 2

        if n <= 3:
            self.nums[n - 1] = n
            return n

        if self.nums[n - 1] != 0:
            return self.nums[n - 1]
        ans = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.nums[n - 1] = ans
        return ans
