class TrieNode:
    def __init__(self):
        self.childs = {}
        self.match_dict = False
        self.leaf = False


class Solution:
    def __init__(self):
        self.trie = TrieNode()
        self.dicts = {}

    def insert(self, word: str) -> str:
        node = self.trie
        s = ""
        for w in word:
            if w not in node.childs:
                node.childs[w] = TrieNode()
            if s in self.dicts:
                self.match_dict = True
                break
            node = node.childs[w]
            s += w
        node.leaf = True
        return s

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for d in dictionary:
            self.dicts.setdefault(d, True)

        ans = []
        for s in sentence.split(" "):
            ns = self.insert(s)
            ans += [ns]
        return " ".join(ans)
