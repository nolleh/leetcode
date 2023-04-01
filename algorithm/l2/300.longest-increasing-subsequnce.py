class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # return the length of longest strictly increasing subsequence
        #
        # get memo which is consecutive with me and has maximum value
        def getPrevMax(memo: dict, val: int):
            # print(memo)
            prev = list(map(lambda x: x[1], filter(lambda x: x[0] < val, memo.items())))
            if len(prev) == 0:
                return 0
            # print(prev)
            return max(prev)

        memo = {}
        for n in nums:
            memo[n] = getPrevMax(memo, n) + 1

        # memo = { 10: 0, 9: 0, 2: 0, 5: 2, 3: 2, 7:3, 101:4 }
        # memo = { 10: 0, 9: 0, 2: 0}
        # print(memo.items())
        return max(memo.values())
