class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows = [0 for _ in picture]
        cols = [0 for _ in picture[0]]

        for i in range(len(picture)):
            for j in range(len(picture[i])):
                if 'W' == picture[i][j]:
                    continue
                rows[i] += 1
                cols[j] += 1

        count = 0
        for i in range(len(picture)):
            for j in range(len(picture[i])):
                if 'B' == picture[i][j] and rows[i] == 1 and cols[j] == 1:
                    count+=1
        return count
