/**
 * LRU Cache - LinkedHashMap 사용
 * https://leetcode.com/problems/lru-cache/?envType=study-plan-v2&envId=top-interview-150
 *
 * Time Complexity: O(1) for both get and put
 * Space Complexity: O(capacity)
 */

class LRUCache(val capacity: Int) {
    private val cache = LinkedHashMap<Int, Int>(capacity, 0.75f, true)

    fun get(key: Int): Int {
        return cache.getOrDefault(key, -1)
    }

    fun put(key: Int, value: Int) {
        cache.put(key, value)
        if (cache.size > capacity) {
            val firstKey = cache.keys.first()
            cache.remove(firstKey)
        }
    }
}

/**
 * Alternative: Manual Implementation (MutableMap + MutableList)
 *
 * Time Complexity:
 * - get: O(n) due to list.remove()
 * - put: O(n) due to list.remove()
 * Space Complexity: O(capacity)
 *
 * Note: List.remove()는 O(n)이므로 위의 LinkedHashMap 방식이 더 효율적입니다.
 */
/*
class LRUCache(val capacity: Int) {
    private val elem = mutableMapOf<Int, Int>()
    private var used = mutableListOf<Int>()

    fun get(key: Int): Int {
        if (!elem.contains(key)) {
            return -1
        }
        used.remove(key)
        used.add(key)
        return elem[key]!!
    }

    fun put(key: Int, value: Int) {
        if (elem.contains(key)) {
            // 이미 존재하는 키면 used에서 제거
            used.remove(key)
        } else if (elem.size >= capacity) {
            // 새로운 키인데 capacity 초과 시, 가장 오래된 키 제거
            val oldestKey = used.removeAt(0)
            elem.remove(oldestKey)
        }

        elem[key] = value
        used.add(key)  // 가장 최근으로 추가
    }
}
*/

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
