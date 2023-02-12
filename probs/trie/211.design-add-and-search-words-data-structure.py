class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for w in word:
            if not w in node:
                node[w] = {}
            node = node[w]
        node["$"] = {}

    def search(self, word: str) -> bool:
        def search_in_node(word: str, node):
            for i, w in enumerate(word):
                if not w in node:
                    if w == ".":
                        for c in node:
                            if search_in_node(word[i + 1 :], node[c]):
                                return True
                    return False
                else:
                    node = node[w]
            return "$" in node

        return search_in_node(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
