class Solution:
    def isHappy(self, n: int) -> bool:
        # happy number: starting with any pos #, replace number by the sum of it's digits
        # repeat until number equals 1.  or loop endlessly in a scyle which does not include 1.
        # those numbers for which this process ends in 1 are happy.
        def next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit**2
            return total_sum

        tortoise = n
        hare = next(tortoise)
        while tortoise != hare and hare != 1:
            tortoise = next(tortoise)
            hare = next(next(hare))

        return hare == 1
