from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wc = Counter(words)
        sort = sorted(wc.items(), key = lambda item: (-item[1], item[0]))
        # print(dict(sort))
        
        ans = []
        i = 0
        while i < k:
            ans.append(sort[i][0]) 
            i += 1
        return ans 
