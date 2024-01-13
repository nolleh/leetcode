class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = [], []
        for iv in intervals:
            if iv[1] < newInterval[0]:
                l.append(iv)
            elif iv[0] > newInterval[1]:
                r.append(iv)
            else:
                newInterval = [min(iv[0], newInterval[0]), max(iv[1], newInterval[1])]
        return l + [newInterval] + r 

