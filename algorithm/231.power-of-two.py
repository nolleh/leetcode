class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
         ## bit
        if n == 0:
            return False
        ## keeps rightmost 1 bit and sets all others as 0
		## -n == ~n + 1
        return n & (-n) == n 
