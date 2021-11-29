package main

import (
    "fmt"
    "strings"
)

func main() {
    var n, m int
    fmt.Scanf("%d\n", &n)
    fmt.Scanf("%d\n", &m)
    results := make([]string, n)
    div := m/n
    for i:=0 ; i<n ; i++ {
        results[i] = strings.Repeat("*", div)
    }
    mo := m % n
    for i:=0 ; i<mo ; i++ {
        results[i] += "*"
    }
    for _, item := range results {
        fmt.Println(item)
    }
}
