class Node:
    def __init__(self):
        self.childs = {}
        self.finished = False


class Trie:
    def __init__(self):
        self.n = Node()

    def insert(self, word: str) -> None:
        node = self.n
        for c in word:
            if c not in node.childs:
                node.childs[c] = Node()
            node = node.childs[c]
        node.finished = True

    def search(self, word: str) -> bool:
        node = self.n
        for w in word:
            c = node.childs
            if w not in c:
                return False
            node = c[w]
        return node.finished

    def startsWith(self, prefix: str) -> bool:
        node = self.n
        for c in prefix:
            if c not in node.childs:
                return False
            node = node.childs[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
