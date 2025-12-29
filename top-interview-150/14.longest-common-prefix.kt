class Solution {
    fun longestCommonPrefix(strs: Array<String>): String {

        var answer = ""
        for (i in strs[0].indices) {
            var char = strs[0][i]
            if (strs.all { it.length > i && it[i] == char }) {
                answer += char
            } else {
                break
            }
        }
        return answer

    }
}

