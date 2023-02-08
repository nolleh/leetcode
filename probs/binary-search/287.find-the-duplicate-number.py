class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 'nums range [1,n], (i.e. inclusive)'
        # has 'only one' repeated number. return that.
        # constraint: uses only constant extraspace.

        # inplace (nlog(n)) 
        nums.sort()

        l, r = 0, len(nums)
        while l < r:
            mid = (r - l) // 2 + l
            # if num is acutally smaller than expected, meaning: prior has dups.
            if nums[mid] < mid + 1:
                r = mid
            else:
                l = mid + 1
        return nums[l]
        
