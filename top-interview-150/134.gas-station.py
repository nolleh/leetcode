class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                # runout of gas, have to find a new starting position
                total = 0
                start = i + 1
            # X(-ve) -> Y(-ve) -> A(+ve) -> B(+ve) -> C(+ve)
            # A is always favorable to help us reach the ans, hence elariest point is always better.

            # why we just stop at point c?
            # 1. we already know there is answer. (sum gas)
            # 2. there is only one valid ans, so we will always choose the most faverable ans.
        return start
