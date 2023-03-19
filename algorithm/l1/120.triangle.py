class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        def iter(i: int, j: int):
            if i == 0:
                memo[(i, j)] = triangle[i][0]
                return triangle[i][0]
            if (i, j) in memo:
                return memo[(i, j)]

            acc = sys.maxsize
            if j > 0:
                acc = min(iter(i - 1, j - 1), acc)
            if j < len(triangle[i - 1]):
                acc = min(iter(i - 1, j), acc)
            acc += triangle[i][j]
            memo[(i, j)] = acc
            return acc

        output = sys.maxsize
        for j in range(len(triangle[-1])):
            output = min(iter(len(triangle) - 1, j), output)
        return output
