# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:


class Solution:
    def search(self, reader: "ArrayReader", target: int) -> int:

        l = 0
        r = 1
        # find boundaries
        while reader.get(r) < target:
            l = r
            r = r * 2
        # previous loops termination condition: includes target == reader.get(r)
        # so next while loop should contains r's value
        while l <= r:
            mid = (r - l) // 2 + l
            if target == reader.get(mid):
                return mid
            elif target > reader.get(mid):
                l = mid + 1
            else:
                r = mid - 1
        return -1
