package main

import (
	"fmt"
	"strings"
)

type StartTrack struct {
	Row int
	Col int
}

type WaterTrack struct {
	Row int
	Col int
	Images [][]string
	Starts []StartTrack
}

func (w *WaterTrack) SetStart() {
	for i:=0 ; i<w.Row ; i++ {
		for j:=0 ; j<w.Col ; j++ {
			if w.Images[i][j] == "V" {
				w.Starts = append(w.Starts, StartTrack{
					Row: i,
					Col: j,
				})
			}
		}
	}
}

func (w *WaterTrack) Track(row, index int, isDown bool)  {
	symbol := w.Images[row][index]
	if symbol == "#" && isDown{
		if row-1 < 0 {
			return
		}
		if index-1 >= 0 {
			w.Track(row-1, index-1, false)
		}
		if index+1 < w.Col {
			w.Track(row-1, index+1, false)
		}
	} else if symbol == "." {
		w.Images[row][index] = "V"
		if row+1 < w.Row {
			w.Track(row+1, index, true)
		}
	}
}

func (w *WaterTrack) Run() {
	for _, start := range w.Starts {
		if start.Row+1 < w.Row {
			w.Track(start.Row+1, start.Col, true)
		}
	}
}

func NewWaterTrack(row, col int) *WaterTrack {
	waterTrack := WaterTrack{
		Row: row,
		Col: col,
		Images: make([][]string, row),
		Starts: make([]StartTrack, 0),
	}
	return &waterTrack
}

func main(){
	var row, col int
	fmt.Scanf("%d %d\n", &row, &col)
	waterTrack := NewWaterTrack(row, col)
	for i:=0 ; i<row ; i++ {
		var inp string
		fmt.Scanln(&inp)
		waterTrack.Images[i] = strings.Split(inp, "")
	}
	waterTrack.SetStart()
	waterTrack.Run()
	for _, rows := range waterTrack.Images {
		fmt.Println(strings.Join(rows, ""))
	}

	
}
