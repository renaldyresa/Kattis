package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

type MetaProg struct {
    maps map[string]int
}

func (m *MetaProg) Append(key, value string)  {
    m.maps[key], _ = strconv.Atoi(value)
}

func (m *MetaProg) Eval(queries []string) {
    a, ok1 := m.maps[queries[0]]
    b, ok2 := m.maps[queries[2]]
    if !ok1 || !ok2 {
        fmt.Println("undefined")
        return
    }
    if queries[1] == "<" {
        fmt.Println(a < b)
    } else if queries[1] == ">" {
        fmt.Println(a > b)
    } else {
        fmt.Println(a == b)
    }
}

func NewMetaProg() *MetaProg {
    metaProg := MetaProg{maps: map[string]int{}}
    return &metaProg
}


func main(){
    scanner := bufio.NewScanner(os.Stdin)
    metaProg := NewMetaProg()
    for scanner.Scan() {
        text := scanner.Text()
        queries := strings.Split(text, " ")
        if queries[0] == "define" {
            metaProg.Append(queries[2], queries[1])
        } else if queries[0] == "eval"{
            metaProg.Eval(queries[1:])
        }
    }
}
