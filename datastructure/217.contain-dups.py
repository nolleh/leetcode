class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict:[int, bool] = {}
        
        for n in nums:
          if n in dict:
            return True
          dict[n] = True
        return False
