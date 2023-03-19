class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count("1")
        mask = 1
        output = 0
        for i in range(32):
            if mask & n != 0:
                output += 1
            mask <<= 1
        return output
