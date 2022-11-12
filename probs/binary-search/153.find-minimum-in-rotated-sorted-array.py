# medium

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,1,2]
        # output 1
        # constraints: O(log N)
        # F F F T T 

        l, r, pivot = 0, len(nums), 0

        while l < r:
            mid = (r - l) // 2 + l
            if nums[0] > nums[mid]:
                pivot = mid
                # drop right to find out first T
                r = mid
            else:
                l = mid + 1
        return nums[pivot]
