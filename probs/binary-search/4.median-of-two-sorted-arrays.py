# hard
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # given nums1, nums2: sorted. size => (m, n)
        # return the median of the two sorted findMedianSortedArrays
        # constraints: O(log (m + n))

        # if has even length, then.. [(m+n) // 2 - 1, (m + n) // 2]

        a, b = nums1, nums2
        if len(a) < len(b):
            a, b = b, a
        M = len(a)
        N = len(b)

        total = M + N
        half = total // 2
        l, r = 0, N - 1

        while True:
            i = (r + l) // 2
            j = half - i - 2

            bLpart = b[i] if i >= 0 else float("-infinity")
            bRpart = b[i + 1] if (i + 1) < N else float("infinity")
            aLpart = a[j] if j >= 0 else float("-infinity")
            aRpart = a[j + 1] if (j + 1) < M else float("infinity")

            if bLpart <= aRpart and aLpart <= bRpart:
                if total % 2 == 0:
                    return (max(bLpart, aLpart) + min(bRpart, aRpart)) / 2
                else:
                    return min(bRpart, aRpart)
            elif bLpart > aRpart:
                # too big for b lpart
                r = i - 1
            else:
                l = i + 1
