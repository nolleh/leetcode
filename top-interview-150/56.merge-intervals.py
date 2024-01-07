class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ## [[1,3], [2,6], [8, 10], [15, 18]]
        ## --> [[1,6], [8, 10], [15, 18]] 
        intervals.sort()
        output = [intervals[0]]

        for iv in intervals[1:]:
            # because of sort, we can compare with last one
            if output[-1][1] >= iv[0]:
                # there is overlap
                output[-1][1] = max(output[-1][1], iv[1])
            else:
                output.append(iv)
        return output

