package main

import (
	"fmt"
	"sort"
)

func Sorted(p []Person) []Person {
	sort.Slice(p, func(i, j int) bool {
		return p[i].Kiraki > p[j].Kiraki
	})
	return p
}

func SortedName(names []string) []string {
	sort.Slice(names, func(i, j int) bool {
		return names[i] < names[j]
	})
	return names
}

type Calculate struct {
	Persons map[string][]Person
}

func (cal Calculate) Result() []string {
	result := []string{}
	for _, value := range cal.Persons {
		sortPersons := Sorted(value)
		result = append(result, sortPersons[0].Name)
	}
	return result
}

func NewCalculate() *Calculate {
	cal := Calculate{}
	cal.Persons = map[string][]Person{}
	return &cal
}

type Person struct {
	Name   string
	Kiraki int
}

func main() {
	var num int
	fmt.Scanln(&num)
	cal := NewCalculate()
	for i := 0; i < num; i++ {
		var name, date string
		var kiraki int
		fmt.Scanf("%s %d %s\n", &name, &kiraki, &date)
		person := Person{Name: name, Kiraki: kiraki}
		cal.Persons[date] = append(cal.Persons[date], person)
	}
	result := SortedName(cal.Result())
	fmt.Println(len(result))
	for _, name := range result {
		fmt.Println(name)
	}
}
