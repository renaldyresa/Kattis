package main

import "fmt"

func main(){
    var listGrades = make([]int, 5)
    fmt.Scanf("%d %d %d %d %d\n", &listGrades[0], &listGrades[1], &listGrades[2], &listGrades[3], &listGrades[4])
    var score int
    fmt.Scanln(&score)
    if score >= listGrades[0] {
        fmt.Println("A")
    } else if score >= listGrades[1] {
        fmt.Println("B")
    } else if score >= listGrades[2] {
        fmt.Println("C")
    } else if score >= listGrades[3] {
        fmt.Println("D")
    } else if score >= listGrades[4] {
        fmt.Println("E")
    } else {
        fmt.Println("F")
    }
}
