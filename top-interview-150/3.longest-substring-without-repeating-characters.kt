class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        val map = mutableMapOf<Char, Int>()
        var answer = 0
        var curr = 0  // window start position
        var i = 0

        while (i < s.length) {
            // Found duplicate character
            if (s[i] in map) {
                // Key insight 1: +1 to exclude the duplicate character itself
                // Key insight 2: maxOf ensures window never moves backward
                // (duplicate might be outside current window already)
                curr = maxOf(curr, map[s[i]]!! + 1)
            }

            map[s[i]] = i
            val ln = i - curr + 1

            // Key insight 3: Recording max length at every step guarantees
            // we've already checked all substrings including characters
            // that are about to be removed from the window
            answer = maxOf(answer, ln)
            i++
        }

        return answer
    }
}

