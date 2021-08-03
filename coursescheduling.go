package main

import (
	"fmt"
	"sort"
	"strconv"
)

type Student string

type Students []Student

func (s Students) Contain(mStudent Student) bool {
	for _, student := range s {
		if student == mStudent {
			return true
		}
	}
	return false
}

type Courses struct {
	schedules map[string]Students
}

func (c *Courses) Append(class string, student Student){
	course, ok := c.schedules[class]
	if !ok {
		c.schedules[class] = Students{student}
	} else {
		if !course.Contain(student) {
			c.schedules[class] = append(course, student)
		}
	}
}

func (c *Courses) GetResult()[]string {
	names := make([]string, 0)
	for key, schedules := range c.schedules {
		text := key + " " + strconv.Itoa(len(schedules))
		names = append(names, text)
	}
	sort.Strings(names)
	return names
}

func NewCourses() *Courses {
	courses := Courses{schedules: map[string]Students{}}
	return &courses
}

func main(){
	var totalCase int
	fmt.Scanln(&totalCase)
	courses := NewCourses()
	for i:=0 ; i<totalCase ; i++ {
		var firstname, lastname, class string
		fmt.Scanf("%s %s %s\n", &firstname, &lastname, &class)
		student := Student(firstname+lastname)
		courses.Append(class, student)
	}
	for _, name := range courses.GetResult() {
		fmt.Println(name)
	}
}
