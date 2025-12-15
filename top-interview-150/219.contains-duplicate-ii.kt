class Solution {
    fun containsNearbyDuplicate(nums: IntArray, k: Int): Boolean {
        // Use a hash set to track elements in the current window
        val window = mutableSetOf<Int>()

        for (i in nums.indices) {
            // If current element already exists in window, we found a duplicate
            if (nums[i] in window) {
                return true
            }

            // Add current element to window
            window.add(nums[i])

            // Maintain window size of k+1 (to check distance <= k)
            // Remove the element that's now outside the window
            if (window.size > k) {
                window.remove(nums[i - k])
            }
        }

        return false
    }
}

// Alternative approach: Using HashMap to track last seen index
// class Solution {
//     fun containsNearbyDuplicate(nums: IntArray, k: Int): Boolean {
//         val lastSeen = mutableMapOf<Int, Int>()
//
//         for (i in nums.indices) {
//             if (nums[i] in lastSeen) {
//                 val lastIndex = lastSeen[nums[i]]!!
//                 if (i - lastIndex <= k) {
//                     return true
//                 }
//             }
//             lastSeen[nums[i]] = i
//         }
//
//         return false
//     }
// }
