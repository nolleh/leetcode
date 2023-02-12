## hard


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotated num array, but can be duplicated.
        # if it duplicated with zero indexed data and is rotated,
        # we couldn't throw away any part!
        # ex. [10,1,10,10,10]
        #               ^
        l, r, pivot = 0, len(nums), 0

        while l < r:
            mid = (r - l) // 2 + l
            if nums[mid] < nums[0]:
                pivot = mid
                r = mid
            elif mid != 0 and nums[mid] == nums[0]:
                i = 1
                while (mid - i > 0 and nums[mid - i] == nums[mid]) and (
                    mid + i < len(nums) and nums[mid + i] == nums[mid]
                ):
                    i += 1
                if nums[mid - i] < nums[0]:
                    pivot = mid - i
                    r = mid
                else:
                    l = mid + 1
            else:
                l = mid + 1

        return nums[pivot]
