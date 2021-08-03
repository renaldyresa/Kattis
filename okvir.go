package main

import (
	"fmt"
	"strings"
)

func main(){
	var row, col int
	fmt.Scanf("%d %d\n", &row, &col)
	var a, b, c, d int
	fmt.Scanf("%d %d %d %d\n", &a, &b, &c, &d)
	words := make([]string, 0)
	for i:=0 ; i<row ; i++ {
		var word string
		fmt.Scanln(&word)
		words = append(words, word)
	}
	totalRow, totalCol := row+a+d, col+b+c
	results := make([][]string, totalRow)
	for i:=0 ; i<totalRow ; i++ {
		results[i] = make([]string, totalCol)
		for j:=0 ; j<totalCol ; j++ {
			if i%2 == 0 {
				item := "#"
				if j%2 == 1 {
					item = "."
				}
				results[i][j] = item
			} else {
				item := "."
				if j%2 == 1 {
					item = "#"
				}
				results[i][j] = item
			}
		}
	}
	l := 0
	for i:=a ; i<totalRow-d ; i++ {
		k := 0
		for j:=b ; j<totalCol-c ; j++ {
			if l<row && k<col {
				results[i][j] = string(words[l][k])
			}
			k++
		}
		l++
	}
	for i:=0 ; i<totalRow ; i++ {
		fmt.Println(strings.Join(results[i], ""))
	}
}
