class Solution {
    fun canConstruct(ransomNote: String, magazine: String): Boolean {
        val freq = mutableMapOf<Char, Int>()

        // Count frequency of each character in magazine
        for (char in magazine) {
            freq[char] = freq.getOrDefault(char, 0) + 1
        }

        // Check if we can construct ransomNote
        for (char in ransomNote) {
            val count = freq.getOrDefault(char, 0)
            if (count <= 0) {
                return false
            }
            freq[char] = count - 1
        }

        return true
    }
}

// Alternative: More concise version using groupingBy
// class Solution {
//     fun canConstruct(ransomNote: String, magazine: String): Boolean {
//         val freq = magazine.groupingBy { it }.eachCount().toMutableMap()
//
//         for (char in ransomNote) {
//             val count = freq.getOrDefault(char, 0)
//             if (count <= 0) return false
//             freq[char] = count - 1
//         }
//
//         return true
//     }
// }

