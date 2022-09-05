class Solution:
    def firstBadVersion(self, n: int) -> int:
        min = 0
        max = n
        
        while min < max:
            mid = (max - min) // 2 + min
            # if you find bad version then drops futher versions and 
            # even you found the bad version and it continues the loop
            # and update min values.
            # this will update the min value as 'first bad version'
            if isBadVersion(mid):
                max = mid
            else:
                min = mid + 1
        return min      
