class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 1. non decreasing order
        # 2. return lexicoraphically grater than 'target'
        l, r = 0, len(letters)
        found = False 
        while l < r:
            mid = (r - l) // 2 + l
            if target < letters[mid]:
                r = mid
                found = True
            else:
                l = mid + 1
        # if the target == letters[mid], then l was added and escaped loop when the letter is bigger.
        return letters[l] if found else letters[0]
