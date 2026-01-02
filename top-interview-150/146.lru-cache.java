import java.util.LinkedHashMap;

/**
 * LRU Cache - Java Implementation
 * https://leetcode.com/problems/lru-cache/?envType=study-plan-v2&envId=top-interview-150
 *
 * Time Complexity: O(1) for both get and put
 * Space Complexity: O(capacity)
 */

class LRUCache {
    private int capacity;
    private LinkedHashMap<Integer, Integer> cache;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new LinkedHashMap<>(capacity, 0.75f, true);
    }

    public int get(int key) {
        return cache.getOrDefault(key, -1);
    }

    public void put(int key, int value) {
        cache.put(key, value);
        if (cache.size() > capacity) {
            int firstKey = cache.keySet().iterator().next();
            cache.remove(firstKey);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */

