package main

import (
    "bufio"
    "fmt"
    "os"
)

var smiles = []string{":)", ";)", ":-)", ";-)"}

func isSmile(text string) bool {
    for _, smile := range smiles {
        if text == smile {
            return true
        }
    }
    return false
}

func main() {
    reader := bufio.NewReader(os.Stdin)
    text, _ := reader.ReadString('\n')
    text = text[:len(text)-1]+"aa"
    for i:=0 ; i<len(text)-2 ; i++ {
        if isSmile(text[i:i+2]) {
            fmt.Println(i)
        } else if isSmile(text[i:i+3]){
            fmt.Println(i)
        }
        
    }
}
