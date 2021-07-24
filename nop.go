package main

import (
    "fmt"
)

var limitUpper = rune(90) 

func main() {
    var instruction string
    fmt.Scanln(&instruction)
    insList := []int{}
    for i, ch := range instruction {
        if limitUpper >= ch {
            insList = append(insList, i)
        }
    }

    var numF = 0
    var result = 0
    for i, ins := range insList {
        if i == 0 {
            continue
        } 
        ind := 1
        temp := numF + (ins - insList[i-1])
        n := 0
        for {
            nm := 4 * ind
            n = numF + nm - temp
            if -1 < n &&  n < 4 {
                numF += nm
                break
            }
            ind++
        }
        result += n
    }
    fmt.Println(result)
}
