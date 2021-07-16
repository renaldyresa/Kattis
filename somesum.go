package main

import (
	"fmt"
)

func main() {
	var num int
	fmt.Scanf("%d\n", &num)
	r := num % 4
	if r == 0 {
		fmt.Println("Even")
	} else if r == 2 {
		fmt.Println("Odd")
	} else {
		fmt.Println("Either")
	}
}
