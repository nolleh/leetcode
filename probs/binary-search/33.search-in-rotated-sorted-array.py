# medium

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums are rotated. with some 'k' pivot
        # after the possible rotation and an integer 'target', return the index of 'target' if it is in nums, or return -1 
        # contratints : O(logN) -> do not sort
        
        # [4,5,6,7,0,1,2] target = 0

        # 1. first traverse nums to findout pivot
        pivot, left, right = 0, 0, len(nums) -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[0]:
                pivot = mid
                right = mid -1
            else:
                left = mid + 1

        left = pivot
        right = pivot + len(nums) -1

        while left <= right:
            mid = left + (right - left) // 2 
            actual_idx = mid % len(nums)

            if target == nums[actual_idx]:
                return actual_idx
            elif target > nums[actual_idx]:
                left = mid + 1
            else:
                right = mid - 1
        return -1
