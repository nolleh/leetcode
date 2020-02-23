package leetcode

func numTrees(n int) int {
    return count(0, n + 1)
}

// 빠르진 않음. 
// Runtime: 3776 ms, faster than 5.55%
// Memory Usage: 1.9 MB, less than 100.00%
// 피봇 가지수 * left 의 가지수 * right 의 가지수
func count(start int, end int) int {
    lefts := 0
    rights := 0
    cnt := 0
    
    if end - start <= 1 {
        return 1
    }

    for p := start + 1; p < end; p++ {
        lefts = count(start, p) 
        rights = count(p, end) 
        cnt += lefts * rights
    }
    return cnt
}
