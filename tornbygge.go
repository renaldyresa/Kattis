package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

func main() {
    var inpNum string
    fmt.Scanln(&inpNum)
    var listInpNum string
    reader := bufio.NewReader(os.Stdin)
    listInpNum, _ = reader.ReadString('\n')
    listInpNum = strings.TrimSuffix(listInpNum, "\n")
    listNum := strings.Split(listInpNum, " ")
    result := 0
    var numTem int
    for _, num := range listNum {
        numInt, _ := strconv.Atoi(num)
        if numInt > numTem {
            result += 1
        }
        numTem = numInt

    }
    fmt.Println(result)
}
