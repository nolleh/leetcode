class Solution:
    def reverseWords(self, s: str) -> str:
        words = [ss.strip() for ss in s.split(" ") if ss.strip()]
        words.reverse()
        return " ".join(words)

    def reverseWordsTwoPointer(self, s: str) -> str:
        """
        Two pointer approach: scan from right to left
        Time: O(n), Space: O(n) for result string
        """
        n = len(s)
        result = []

        # Start from the end
        i = n - 1

        while i >= 0:
            # Skip trailing/leading spaces
            while i >= 0 and s[i] == " ":
                i -= 1

            if i < 0:
                break

            # Find the end of current word (right pointer)
            j = i

            # Find the start of current word (left pointer)
            while i >= 0 and s[i] != " ":
                i -= 1

            # Extract word: s[i+1:j+1]
            word = s[i + 1 : j + 1]
            result.append(word)

        return " ".join(result)
