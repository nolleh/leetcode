# EASY
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # get pivot where sum of left / right is same
        # get lreft most pivot index. if not exists, then return -1
        
        #  [x+1 if x >= 45 else x+5 for x in l]
        
        # pivots = [i for i,_ in enumerate(nums) if sum(nums[:i+1]) == sum(nums[i:])]
        # return pivots[0] if len(pivots) > 0 else -1
        """
        for i in range(len(nums)):
          leftsum = 0
          rightsum = 0
          for l in range(i):
            leftsum += nums[l]
          for r in range(i+1, len(nums)):
            rightsum += nums[r]
          if leftsum == rightsum:
            return i
          
        return -1
        """
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
              return i
            leftsum += x
        return -1
        
