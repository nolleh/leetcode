class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if k >= len(arr):
            return arr

        l, r = 0, len(arr)
        mid = 0
        while l < r:
            mid = (r - l) // 2 + l
            if arr[mid] >= x:
                r = mid
            else:
                l = mid + 1

        nl, nr = l - 1, l

        while nr - nl - 1 < k:
            if nl == -1:
                nr += 1
                continue

            if nr == len(arr) or abs(arr[nl] - x) <= abs(arr[nr] - x):
                nl -= 1
            else:  # unable to access nl
                nr += 1
        return arr[nl + 1 : nr]
