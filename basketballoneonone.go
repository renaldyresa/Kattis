package main

import (
	"fmt"
	"strconv"
)

type Score struct {
	Player1 int
	Player2 int
}

func (sc Score) Validate() bool {
	if sc.Player1 >= 11 && sc.Player1-sc.Player2 >= 2 {
		return true
	}
	if sc.Player2 >= 11 && sc.Player2-sc.Player1 >= 2 {
		return true
	}
	return false
}

func (sc Score) Win() string {
	var result string
	if sc.Player1 > sc.Player2 {
		result = "A"
	} else {
		result = "B"
	}
	return result
}

func calculateScore(score Score, text string) (Score, string) {
	if len(text) <= 0 {
		return score, text
	}
	if score.Validate() {
		return score, text
	}
	player := string(text[0])
	sc, _ := strconv.Atoi(string(text[1]))
	if player == "A" {
		score.Player1 += sc
	} else {
		score.Player2 += sc
	}
	text = text[2:]
	return calculateScore(score, text)
}

func main() {
	var inpText string
	fmt.Scanln(&inpText)
	var score Score
	sc, _ := calculateScore(score, inpText)
	fmt.Println(sc.Win())
}
