class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # new weight = max(x - y, y - x)
        # return last remaining staones weight.
        def remove_largest():
            index_of_largest = stones.index(max(stones))
            # swap
            stones[index_of_largest], stones[-1] = stones[-1], stones[index_of_largest]
            return stones.pop()
        
        while len(stones) > 1:
            n1 = remove_largest()
            n2 = remove_largest()
            if n1 != n2:
                stones.append(n1 - n2)
        return stones[0] if stones else 0
