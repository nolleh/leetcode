class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)

        result = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                result[i + j + 1] += int(num1[i]) * int(num2[j])
                result[i + j] += result[i + j + 1] // 10
                result[i + j + 1] %= 10
        return "".join(map(str, result))
