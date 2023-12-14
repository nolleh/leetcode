class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        minimum = sys.maxsize

        for p in prices:
            if minimum > p:
                minimum = p
            else:
                if output < p - minimum:
                    output = p - minimum
        return output
