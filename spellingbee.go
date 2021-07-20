package main

import (
    "fmt"
)

type SpellBee struct {
    mapWords  map[rune]string
    firstChar byte
}

func (sb *SpellBee) compare(wordDict string) bool {
    if len(wordDict) < 4 {
        return false
    }
    isFirstChar := false
    for _, ch := range wordDict {
        if !isFirstChar {
            if ch == rune(sb.firstChar) {
                isFirstChar = true
            }
        }

        _, ok := sb.mapWords[ch]
        if !ok {
            return false
        }
    }
    return isFirstChar
}

func NewSpellBee(word string) *SpellBee {
    spellBee := SpellBee{}
    spellBee.firstChar = word[0]
    spellBee.mapWords = map[rune]string{}
    for _, ch := range word {
        _, ok := spellBee.mapWords[ch]
        if !ok {
            spellBee.mapWords[ch] = string(ch)
        }
    }
    return &spellBee
}

func main() {
    var word string
    var totalDict int
    fmt.Scanf("%s\n", &word)
    fmt.Scanf("%d\n", &totalDict)
    spellBee := NewSpellBee(word)
    for i := 0; i < totalDict; i++ {
        var wordDict string
        fmt.Scanf("%s\n", &wordDict)
        if spellBee.compare(wordDict) {
            fmt.Println(wordDict)
        }
    }

}
