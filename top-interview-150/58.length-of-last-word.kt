class Solution {
    fun lengthOfLastWord(s: String): Int {
        var length = 0
        var i = s.length - 1

        // Skip trailing spaces
        while (i >= 0 && s[i] == ' ') {
            i--
        }

        // Count the word
        while (i >= 0 && s[i] != ' ') {
            length++
            i--
        }

        return length
    }
}

