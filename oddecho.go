package main

import "fmt"

func main(){
    var totalCase int
    fmt.Scanln(&totalCase)

    for i:=0 ; i<totalCase ; i++ {
        var word string
        fmt.Scanln(&word)
        if i%2 == 0 {
            fmt.Println(word)
        }
    }
}
