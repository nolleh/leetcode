class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1 and nums2 has intersection. return with any order.
        # not sorted, but we can use binary search, after sort. TC: NlogN + logN = Nlog(N)
        nums1.sort()
        s = set()

        for n in nums2:
            if self.bsearch(nums1, n):
                s.add(n)
        return list(s)

    def bsearch(self, nums: List[int], target: int):
        l, r = 0, len(nums)
        while l < r:
            mid = (r - l) // 2 + l

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return False 
