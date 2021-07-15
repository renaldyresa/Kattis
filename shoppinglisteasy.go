package main

import (
    "bufio"
    "fmt"
    "os"
    "sort"
    "strings"
)

func Contains(ls []string, str string) bool {
    for _, val := range ls {
        if val == str {
            return true
        }
    }
    return false
}

type Item struct {
    ListItem []string
}

func (it Item) AddItem(ls []string) []string {
    temList := []string{}
    for _, val := range ls {
        if Contains(it.ListItem, val) {
            temList = append(temList, val)
        }
    }
    return temList
}

func (it Item) GetResult() []string {
    sort.Slice(it.ListItem, func(i, j int) bool {
        return it.ListItem[i] < it.ListItem[j]
    })
    return it.ListItem
}

func NewItem() *Item {
    item := Item{}
    item.ListItem = []string{}
    return &item
}

func main() {
    var num1, num2 int
    fmt.Scanf("%d %d\n", &num1, &num2)
    scanner := bufio.NewScanner(os.Stdin)
    item := NewItem()
    for i := 0; i < num1; i++ {
        var strItems string
        scanner.Scan()
        strItems = scanner.Text()
        listItem := strings.Split(strItems, " ")
        if i == 0 {
            item.ListItem = listItem
        } else {
            item.ListItem = item.AddItem(listItem)
        }
    }
    result := item.GetResult()
    fmt.Println(len(result))
    for _, it := range result {
        fmt.Println(it)
    }
}
