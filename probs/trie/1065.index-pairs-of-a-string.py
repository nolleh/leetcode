class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        # trie.. ? how ?
        ans = []
        # print(words)
        words = sorted(words, key = lambda w : len(w))
        # print(words) 
        for i, t in enumerate(text):
            for word in words: 
                if text[i:i+len(word)] == word:
                    ans += [[i, i+len(word) - 1]]
        return ans 
