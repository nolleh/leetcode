from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        # nums1 has length of m + n, so you can merge in-place.
        i2 = 0
        # for i2 in range(len(nums2)):
        for i, n1 in enumerate(nums1):
            if i >= m or (len(nums2) > i2 and n1 > nums2[i2]):
                for j in range(len(nums1) -1, i, -1):
                    nums1[j] = nums1[j-1]
                nums1[i] = nums2[i2]
                i2+=1
                m+=1
        """
        nums1_copy = nums1[:m]
        p1 = 0
        p2 = 0

        for p in range(n + m):
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
