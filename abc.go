package main

import (
	"fmt"
	"sort"
	"strconv"
)

func main() {
	var a, b, c int
	fmt.Scanf("%d %d %d\n", &a, &b, &c)
	listNum := [3]int{a, b, c}
	sort.Ints(listNum[:])
	var sr string
	fmt.Scanln(&sr)
	mapN := map[byte]int{'A': listNum[0], 'B': listNum[1], 'C': listNum[2]}
	for _, val := range sr {
		switch byte(val) {
		case 'A':
			fmt.Printf("%s ", strconv.Itoa(mapN['A']))
		case 'B':
			fmt.Printf("%s ", strconv.Itoa(mapN['B']))
		case 'C':
			fmt.Printf("%s ", strconv.Itoa(mapN['C']))
		}
	}
}
