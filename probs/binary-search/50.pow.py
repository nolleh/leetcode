class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        current_product = x

        while n > 0:
            if n % 2 == 1:
                ans *= current_product
            current_product *= current_product
            n //= 2
        return ans
