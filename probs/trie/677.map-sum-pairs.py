class Node:
    __slots__ = 'childs', 'val'
    def __init__(self):
        self.childs = {}
        self.val = 0 
class MapSum:
    def __init__(self):
        self.map = {}
        self.root = Node()

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        node = self.root
        node.val += delta
        for w in key:
            node = node.childs.setdefault(w, Node())
            node.val += delta
    
    def sum(self, prefix: str) -> int:
        sum = 0
        node = self.root
        for w in prefix:
            if w not in node.childs:
                return 0
                
            node = node.childs[w] 
            sum = node.val
        return sum    


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
