package main

import (
	"fmt"
	"strconv"
)

var ASCII_CODE = map[string]string{
	"xxxxxx...xx...xx...xx...xx...xxxxxx" : "0",
	"....x....x....x....x....x....x....x" : "1",
	"xxxxx....x....xxxxxxx....x....xxxxx" : "2",
	"xxxxx....x....xxxxxx....x....xxxxxx" : "3",
	"x...xx...xx...xxxxxx....x....x....x" : "4",
	"xxxxxx....x....xxxxx....x....xxxxxx" : "5",
	"xxxxxx....x....xxxxxx...xx...xxxxxx" : "6",
	"xxxxx....x....x....x....x....x....x" : "7",
	"xxxxxx...xx...xxxxxxx...xx...xxxxxx" : "8",
	"xxxxxx...xx...xxxxxx....x....xxxxxx" : "9",
}

var ASCII_DECODE = map[string]string{
	"0" : "xxxxxx...xx...xx...xx...xx...xxxxxx",
	"1" : "....x....x....x....x....x....x....x",
	"2" : "xxxxx....x....xxxxxxx....x....xxxxx",
	"3" : "xxxxx....x....xxxxxx....x....xxxxxx",
	"4" : "x...xx...xx...xxxxxx....x....x....x",
	"5" : "xxxxxx....x....xxxxx....x....xxxxxx",
	"6" : "xxxxxx....x....xxxxxx...xx...xxxxxx",
	"7" : "xxxxx....x....x....x....x....x....x",
	"8" : "xxxxxx...xx...xxxxxxx...xx...xxxxxx",
	"9" : "xxxxxx...xx...xxxxxx....x....xxxxxx",
}


func main() {
	numbers := []string{}
	var totalNumber int
	for i:=0 ; i<7 ; i++ {
		var line string
		fmt.Scanln(&line)
		line += "."
		totalLine := len(line)
		if i == 0 {
			totalNumber = totalLine/6
			for j:=0 ; j<totalNumber ; j++ {
				numbers = append(numbers, "")
			}
		}
		for j:=0 ; j<totalNumber ; j++ {
			numbers[j] += line[j*6:(j+1)*6-1]
		}
	}
	var numA, numB string
	isNumB := false
	for _, val := range numbers {
		num, ok := ASCII_CODE[val]
		if ok {
			if isNumB {
				numB += num
			} else {
				numA += num
			}
		} else {
			isNumB = true
		}
	}
	numAInt, _ := strconv.Atoi(numA)
	numBInt, _ := strconv.Atoi(numB)
	numResult := numAInt + numBInt
	numResStr := strconv.Itoa(numResult)
	for i:=0 ; i<7 ; i++ {
		resultStr := ""
		for _, ch := range numResStr{
			val, _ := ASCII_DECODE[string(ch)]
			resultStr += val[i*5:(i+1)*5]
			resultStr += "."
		}
		fmt.Println(resultStr[:len(resultStr)-1])
	}
}
