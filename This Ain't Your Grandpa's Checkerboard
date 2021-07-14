package main

import "fmt"

func main() {
	var inpNum int
	fmt.Scanln(&inpNum)
	sBlock := make([]string, inpNum)
	for i:=0; i<inpNum; i++ {
		fmt.Scanln(&sBlock[i])
	}
	var result = 1
	var white, black = "W", "B"
	var countWhite, countBlack = 0, 0
	for i := range sBlock {
		var tcrWhite, tcrBlack = 0, 0
		var tccWhite, tccBlack = 0, 0
		var colorRBefore, colorCBefore string
		var ccColor, crColor = 0, 0
		isValid := true
		for j := range sBlock[i]{
			if string(sBlock[i][j]) == white {
				if i == 0 {
					countWhite++
				}
				if colorRBefore == white{
					crColor++
				} else {
					crColor = 1
				}
				colorRBefore = white
				tcrWhite++
			} else {
				if i == 0 {
					countBlack++
				}
				if colorRBefore == black {
					crColor++
				} else {
					crColor = 1
				}
				colorRBefore = black
				tcrBlack++
			}
			if string(sBlock[j][i]) == white {
				if colorCBefore == white {
					ccColor++
				} else {
					ccColor = 1
				}
				colorCBefore = white
				tccWhite++
			} else {
				if colorCBefore == black {
					ccColor++
				} else {
					ccColor = 1
				}
				colorCBefore = black
				tccBlack++
			}
			if ccColor >= 3 || crColor >= 3 {
				isValid = false
				break
			}
		}
		if countWhite != tcrWhite || countBlack != tcrBlack ||
			countWhite != tccWhite || countBlack != tccBlack ||
			!isValid {
			result = 0
			break
		}
	}
	fmt.Println(result)

}
