class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # permute. all possible order
        output = {}

        def iter(curr: List[int], remains: List[int]):
            if len(remains) == 0:
                output[f"{curr}"] = curr

            for i in range(len(remains)):
                cur = curr + [remains[i]]
                iter(cur, remains[:i] + remains[i + 1 :])

        iter([], nums)
        return output.values()
