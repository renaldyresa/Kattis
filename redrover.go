package main

import (
	"fmt"
	"strings"
)

type RedRover struct {
	mapCode map[string]int
	code string
}

func (rr *RedRover) setCodes(code string, k int) {
	rr.code = code
	for i:=k ; i<len(code)+1 ; i++ {
		key := code[i-k:i]
		_, ok := rr.mapCode[key]
		if ok {
			rr.mapCode[key] += 1
		} else {
			rr.mapCode[key] = 1
		}
	}
}

func (rr *RedRover) getResult() int {
	var result int
	var max int
	var microCode string
	for key, val := range rr.mapCode {
		if max < val {
			max = val
			microCode = key
		}
	}
	decode := strings.ReplaceAll(rr.code, microCode, "M")
	result = len(decode) + len(microCode)
	return result
}

func NewRedRover() *RedRover {
	redRover := RedRover{}
	redRover.mapCode = map[string]int{}
	return &redRover
}

func main() {
	var code string
	fmt.Scanln(&code)
	var best int
	lenCode := len(code)
	if lenCode <= 4 {
		best = lenCode
	} else {
		for i:=2 ; i<len(code) ; i++ {
			redRover := NewRedRover()
			redRover.setCodes(code, i)
			res := redRover.getResult()
			if i == 2 {
				best = res
			} else {
				if best > res {
					best = res
				}
			}
		}
	}
	fmt.Println(best)
}
