package problem3446

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func sortMatrix(grid [][]int) [][]int {
	n := len(grid)
	for i := range 2*n - 1 {
		var row, col int
		if i < n {
			row, col = i, 0
		} else {
			row, col = 0, i-n+1
		}
		var diagonal []int
		for r, c := row, col; r < n && c < n; r, c = r+1, c+1 {
			diagonal = append(diagonal, grid[r][c])
		}
		if i < n {
			sort.Sort(sort.Reverse(sort.IntSlice(diagonal)))
		} else {
			sort.Ints(diagonal)
		}
		for _, v := range diagonal {
			grid[row][col] = v
			row++
			col++
		}
	}
	return grid
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return sortMatrix(grid)
}
