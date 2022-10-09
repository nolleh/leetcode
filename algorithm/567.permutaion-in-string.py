class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sc = collections.Counter(s1)
        sl = len(s1)
        for i in range(len(s2)):
            sc2 = collections.Counter(s2[i:i+sl])
            if sc == sc2:
                return True
        return False
