from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # c in s can be changed to any letter for k times
        # return # of longest repeating character
        
        left = maxf = res = 0
        counter = defaultdict(int)
        
        for right in range(len(s)):
            counter[s[right]] += 1
            maxf = max(maxf, counter[s[right]])
            while (right - left + 1) - maxf > k:
                counter[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res
        
        # 1. for c in s, count max_window (k change, lrc repeated)
        # 2. if the cur_window is smaller than max_window, then do not add to dict
        # 3. return dict[max_window]
        
        #max_window = 0
        #for i in range(len(s)):
        #    c = s[i] 
        #    cur_window = 0
        #    remain = k
        #    for w in range(len(s) - i + 1):
        #        if i + w - 1 < 0:
        #            continue
        #        if c != s[i + w -1]:
        #            if remain > 0:
        #                remain -= 1
        #            else:
        #                break
        #        cur_window += 1
        #    max_window = max(max_window, cur_window)
        #return max_window
