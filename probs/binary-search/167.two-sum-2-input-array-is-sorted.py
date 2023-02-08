class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non-decreasing order
        # find two numbers such that they add up to a specific target number
        # return indices. exactly one solution.
        # SC should be O(1)
        for i,n in enumerate(numbers):
            l, r = i + 1, len(numbers)
            while l < r:
                mid = (r - l) // 2 + l
                if i == mid:
                    continue 
                if target == n + numbers[mid]:
                    return [i + 1, mid + 1]
                elif target > n + numbers[mid]:
                    l = mid + 1
                else:
                    r = mid
            
        return [-1, -1]
