class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            # Quick response for empty list
            return 0

        n = len(nums)

        # record of length of increasing subsequence
        length = [1 for _ in range(n)]

        # record the path count of increasing subsequence
        count = [1 for _ in range(n)]

        # scan each number, where increasing subsequence ending in nums[i]
        for i in range(n):
            # for every number before nums[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    # nums[j] can add to increasing subsequence ending in nums[i]

                    if (length[j] + 1) > length[i]:
                        # nums[j] make it longer to increasing subsequence ending in nums[i]
                        length[i], count[i] = length[j] + 1, count[j]

                    elif (length[j] + 1) == length[i]:
                        # nums[j] add some new paths of increasing subsequence ending in nums[i]
                        count[i] += count[j]

        # get the length of lonest increasing subsequence
        max_length = max(length)

        # report total path count of longest increasing subsequence
        return sum(
            count for length, count in zip(length, count) if length == max_length
        )
