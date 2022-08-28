class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
       # 1. preserve order
        # 2. charater
        
        mapper: [char, char] = {}
        mapped: [char, char] = {}
        
        for i, sc in enumerate(s):
            if sc in mapper:
                if mapper[sc] != t[i]:
                    return False
            elif t[i] in mapped:
                if mapped[t[i]] != s[i]:
                    return False
            else:
                mapper[sc] = t[i]
                mapped[t[i]] = sc
        return True
