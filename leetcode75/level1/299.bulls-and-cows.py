from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # bulls: # of correct value and position
        # cows: # of incorrect position but correct value
        # xAyB: x : bulls, y : cows
        # 1122, 1222 => 3A1B
        bulls = cows = 0
        sc = Counter(secret)

        for i, g in enumerate(guess):
            if secret[i] == g:
                bulls += 1
                # update the cows
                # if all g characters from secret were used up
                cows -= int(sc[g] <= 0)
            else:
                cows += int(sc[g] > 0)
            sc[g] -= 1
        # return str(bulls) + 'A' + str(cows) + 'B'
        return "{}A{}B".format(bulls, cows)
