class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # peak element: strictly greater than its neighbors.
        # find peak elements, and return its index. 
        # constraints: O(log N) 
		# all array boundaries are -infinite

        # [1,2,3,1] => 3 (return idx - 2)
        # [1,2,1,3,5,6,4] => 2 or 6 (return idx - 1 or 5)

        l, r = 0, len(nums)-1
        while l < r:
            mid = (r - l) // 2 + l
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l    
