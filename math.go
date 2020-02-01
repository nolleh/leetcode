package leetcode

func C(n int, r int) int {
    // return factorial(n) / (factorial(n - r) * factorial(r))
    return factuntil(n, n-r) / factorial(r)
}

func factorial(n int) int {
    fact := 1
    for i := 1; i <= n; i++ {
        fact *= i
    }
    return fact
}

func factuntil(n int, u int) int {
    fact := 1
    for i := n; i > u; i-- {
        fact *= i
    }
    return fact
}