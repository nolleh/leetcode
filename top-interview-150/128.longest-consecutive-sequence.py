class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()

        for n in nums:
            s.add(n)

        ans = 0
        for n in nums:
            if not n - 1 in s:
                cnt = 1
                i = 1
                while n + i in s:
                    cnt += 1
                    i += 1
                ans = max(ans, cnt)
        return ans
