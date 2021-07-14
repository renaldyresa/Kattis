package main

import (
	"fmt"
	"strconv"
)

func calculate(num string) string {
	result := string(num[0])
	for i:=1 ; i<len(num) ; i++ {
		if string(num[i]) != "0" {
			a, _ := strconv.Atoi(result)
			b, _ := strconv.Atoi(string(num[i]))
			result = strconv.Itoa(a * b)
		}
	}
	if len(result) != 1 {
		return calculate(result)
	}
	return result
}

func main() {
	var inpNum string
	fmt.Scanln(&inpNum)
	result := calculate(inpNum)
	fmt.Println(result)
}
