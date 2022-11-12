# medium

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if 1 == len(nums):
            return [0, 0] if target == nums[0] else [-1, -1]
        
        begin, end = 0, len(nums) - 1
        first = -1
        while begin <= end:
            mid = (end - begin) // 2 + begin
            if target == nums[mid]:
                if mid == begin or target > nums[mid - 1]:
                    first = mid
                    break
                end = mid - 1
            elif target > nums[mid]:
                begin = mid + 1
            else:
                end = mid - 1

        end = len(nums) - 1
        last = -1
        if begin == -1:
            return [-1, -1]

        begin = 0 
        while begin <= end:
            mid = (end - begin) // 2 + begin
            if target == nums[mid]:
                if mid == end or target < nums[mid + 1]:
                    last = mid
                    break
                begin = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                begin = mid + 1
        return [first, last]
