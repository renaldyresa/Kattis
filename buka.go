package main

import (
    "fmt"
)

func main() {
    var number1, number2, operation, result string
    fmt.Scanln(&number1)
    fmt.Scanln(&operation)
    fmt.Scanln(&number2)
    if operation == "*" {
        result = number1 + number2[1:]
    } else {
        lenA := len(number1)
        lenB := len(number2)
        if lenA < lenB {
            result = number2[:(lenB-lenA)] + number1
        } else if lenA > lenB {
            result = number1[:(lenA-lenB)] + number2
        } else {
            result = "2" + number1[1:]
        }
    }
    fmt.Println(result)
}
