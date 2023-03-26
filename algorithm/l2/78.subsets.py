class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        def iter(curr: List[int], fst: int):
            for i in range(fst, len(nums)):
                output.append(curr + [nums[i]])
                iter(curr + [nums[i]], i + 1)

        iter([], 0)
        return output
