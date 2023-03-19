class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # TLE
        # dict = {}
        # for i in range(0, len(nums) - 1):
        #    for j in range(i + 1, len(nums)):
        #        key = -1 * (nums[i] + nums[j])
        #        if key not in dict:
        #            dict[key] = []
        #        dict[key].append([i, j])
        ## dict: O(N * N)
        # output = {}
        # for i, n in enumerate(nums):
        #    if n in dict:
        #        for pair in dict[n]:
        #            if i not in pair:
        #                temp = [nums[pair[0]], nums[pair[1]], nums[i]]
        #                temp.sort()
        #                key = ','.join(list(map(lambda x: str(x),temp)))
        #                #if key not in output:
        #                output[key] = temp
        # return output.values()
        res = []
        nums.sort()
        if len(nums) < 3:
            return res

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return res
