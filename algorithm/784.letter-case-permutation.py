class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(curr: str):
            if len(curr) == len(s):
                output.append(curr[:])
                return
            i = len(curr)
            if s[i].isalpha():
                backtrack(curr + s[i].upper())
                backtrack(curr + s[i].lower())
            else:
                backtrack(curr + s[i]) 

        output = [] 
        backtrack('')
        return output
