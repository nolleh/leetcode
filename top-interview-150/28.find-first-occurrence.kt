class Solution {
    // Sliding Window approach
    // Time: O(n * m) where n = haystack.length, m = needle.length
    // Space: O(1)
    fun strStr(haystack: String, needle: String): Int {
        if (needle.length > haystack.length) {
            return -1
        }
        var l = 0
        var r = needle.length - 1

        while (r < haystack.length) {
            var found = true
            for (i in l..r) {
                if (haystack[i] != needle[i - l]) {  // i - l converts to needle index
                    found = false
                    break
                }
            }

            if (found) return l

            l++
            r++
        }
        return -1
    }
}

