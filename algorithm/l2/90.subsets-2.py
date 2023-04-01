class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # check [4,4,4,1,4]
        nums.sort()
        output = {}
        output[""] = []

        def iter(curr: List[int], fst: int):
            for i in range(fst, len(nums)):
                cur = curr + [nums[i]]
                output[f"{cur}"] = cur
                iter(cur, i + 1)

        iter([], 0)
        return output.values()
