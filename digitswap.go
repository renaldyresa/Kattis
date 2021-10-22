package main

import (
    "fmt"
)

func main() {
    var input string
    fmt.Scanln(&input)

    for i:=0 ; i<len(input) ; i++ {
        fmt.Print(string(input[(len(input)-1)-i]))
    }

}
