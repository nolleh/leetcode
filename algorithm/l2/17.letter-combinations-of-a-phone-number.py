class Solution:
    def permu(self, ind, digits, ans, ds, mapping):
        if len(ds) == len(digits):
            ans.append(ds)
            return

        for i in range(len(mapping[digits[ind]])):
            ds += list(mapping[digits[ind]])[i]
            self.permu(ind + 1, digits, ans, ds, mapping)
            ds = ds[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if len(digits) == 1:
            return [x for x in mapping[digits]]
        ans = []
        ds = ""

        self.permu(0, digits, ans, ds, mapping)

        return ans
