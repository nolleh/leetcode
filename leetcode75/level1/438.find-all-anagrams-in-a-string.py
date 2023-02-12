from collections import defaultdict, Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        s_count = Counter()

        output = []
        for i in range(ns):
            s_count[s[i]] += 1

            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1
            if p_count == s_count:
                output.append(i - np + 1)

        return output

        # def isAnagram(a: str, b: str) -> bool:
        #    if len(a) != len(b):
        #        return False
        #    dict = defaultdict(int)
        #    for a_s in a:
        #        dict[a_s] += 1
        #
        #    for b_s in b:
        #        if b_s not in dict:
        #            return False
        #        if dict[b_s] <= 0:
        #            return False
        #        dict[b_s] -= 1
        #    return True
        #
        # ans = []
        # for i in range(len(s)):
        #    sub_s = s[i:i + len(p)]
        #    if isAnagram(sub_s, p):
        #        ans += [i]
        # return ans
