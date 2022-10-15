class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        if 1 == len(s):
           return 1
        for i in range(len(s)):
            dict = {}
            for w in range(i + 1, len(s) + 1):
                if s[w -1] in dict:
                    break
                ns = s[i:w]
                dict[s[w-1]] = True
            #print(maxlen, dict.keys())
            maxlen = max(maxlen,len(dict.keys()))
        return maxlen
