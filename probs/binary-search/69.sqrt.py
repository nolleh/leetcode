## easy


class Solution:
    def mySqrt(self, x: int) -> int:
        # return square root of x rounded down to the nearest integer.
        # returned integer should be non-negative.
        l, r = 0, x
        if x == 1:
            return 1

        while l < r:
            mid = (r - l) // 2 + l
            square = mid * mid
            if x == square:
                return mid
            elif x > square:
                l = mid + 1
            else:
                r = mid
        return r - 1 if r > 1 else 0
