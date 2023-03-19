class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first=1, curr=[]):
            if len(curr) == k:
                ## append: mutate the old list. (inplace)
                output.append(curr[:])
                ## plus: does not mutate.
                # output += curr[:]

            for i in range(first, n + 1):
                curr += [i]
                # repeate for remain values
                backtrack(i + 1, curr)
                # remove last value for backtrack
                curr.pop()

        output = []
        backtrack()
        return output
