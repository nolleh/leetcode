class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        md = {}
        md2 = {}
        sp = s.split(' ')

        if len(pattern) != len(sp):
            return False

		# you can also consider zip
		# for c,w in zip(pattern, words):
		#   if c not in md:
        #      if w in md2: ...
        for i, p in enumerate(sp):
            if pattern[i] not in md:
                if p in md2:
                    return False
                md[pattern[i]] = p
                md2[p] = pattern[i]
            if md[pattern[i]] != p:
                return False
        return True
