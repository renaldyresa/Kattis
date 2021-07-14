package main

import (
    "fmt"
)

func main() {
    var number int
    fmt.Scan(&number)

    var num = 1
    var sNumber int
    var result []int
    for i:=0 ; i<number ; i++ {
        fmt.Scan(&sNumber)
        for num < sNumber {
            result = append(result, num)
            num++
        }
        num = sNumber
        num++

    }
    if len(result) == 0 {
        fmt.Printf("good job")
    }else {
        for _, i := range result {
            fmt.Printf("%v \n", i)
        }
    }

}
