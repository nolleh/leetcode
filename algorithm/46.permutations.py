class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr: List[int], remains: List[int]):
            if len(remains) == 0:
                output.append(curr[:])

            for i in range(len(remains)):
                curr += [remains[i]]
                backtrack(curr, remains[:i] + remains[i+1:])
                curr.pop()
        output = [] 
        backtrack([], nums)
        return output
