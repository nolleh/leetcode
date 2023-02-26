class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # return an array such that answer[i] is the number of days 
        # you have to wait after ith day to get a warmer temperature.

        # Input: temperatures = [73,74,75,71,69,72,76,73]
        # Output: [1,1,4,2,1,1,0,0]

        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures) -1, -1, -1):
            while stack and temperatures[i] >= stack[-1][1]:
                stack.pop()
            
            if stack:
                res[i] = stack[-1][0] - i

            stack.append((i, temperatures[i]))
        return res
