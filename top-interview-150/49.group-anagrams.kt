class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        val map = mutableMapOf<String, List<String>>()
        for (str in strs) {
            val key = str.toCharArray().sorted().joinToString("")
            map[key] = map.getOrDefault(key, emptyList()) + str
        }
        return map.values.toList()
    }
}

