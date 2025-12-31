class Solution {
    fun minWindow(s: String, t: String): String {
        val tmap = mutableMapOf<Char, Int>()
        for (c in t) {
            tmap[c] = tmap.getOrDefault(c, 0) + 1
        }

        var left = 0
        var right = 0
        var minLength = Int.MAX_VALUE
        var minStart = 0
        var smap = mutableMapOf<Char, Int>()

        val required = tmap.size
        var formed = 0

        while (right < s.length) {
            // find window that contains all characters in t
            if (s[right] in tmap) {
                smap[s[right]] = smap.getOrDefault(s[right], 0) + 1
                if (smap[s[right]] == tmap[s[right]]) {
                    formed++
                }
                // validate window
                while (formed == required) {
                    // if window is valid, update minLength and minStart
                    if (right - left + 1 < minLength) {
                        minLength = right - left + 1
                        minStart = left
                    }
                    // move left pointer to find the smallest window
                    if (smap.contains(s[left])) {
                        if (smap[s[left]] == tmap[s[left]]) {
                            formed--
                        }
                        smap[s[left]] = smap[s[left]]!! - 1
                        if (smap[s[left]]!! <= 0) {
                            smap.remove(s[left])
                        }
                    }
                    left++
                }
            }
            right++
        }
        return if (minLength == Int.MAX_VALUE) "" else s.substring(minStart, minStart + minLength)
    }
}

