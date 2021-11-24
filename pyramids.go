package main

import "fmt"

func main()  {
    var n int
    fmt.Scanln(&n)
    var height, numBlock int
    i := 1
    for {
        numBlock += i*i
        if numBlock > n {
            break
        }
        height += 1
        i += 2
    }
    fmt.Println(height)
}
