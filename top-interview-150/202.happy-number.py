class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            n = self._sum_of_squares(n)

        return True

    def _sum_of_squares(self, num: int) -> int:
        """Helper function to calculate sum of squares of digits"""
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
