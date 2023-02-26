package leetcode

import "strconv"

func str2Int(str string) int {
    n := 0
    for i := 0; i < len(str); i++ {
        a, _ := strconv.Atoi(string(str[i]))
        n += a * pow(10, len(str) -i -1)
    }
    return n
}
