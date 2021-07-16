package main

import (
    "fmt"
)

func main() {
    var a, b, c, n int
    fmt.Scanf("%d %d %d %d\n", &a, &b, &c, &n)
    if n < 3 {
        fmt.Println("NO")
    } else if a == 0 || b == 0 || c == 0 || a+b+c < n {
        fmt.Println("NO")
    } else {
        fmt.Println("YES")
    }

}
