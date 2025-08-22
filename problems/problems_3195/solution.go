package problem3195

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumArea(grid [][]int) int {
	left, right, top, bottom := len(grid[0]), 0, len(grid), 0
	for i, row := range grid {
		for j, val := range row {
			if val == 1 {
				left = min(left, j)
				right = max(right, j)
				top = min(top, i)
				bottom = max(bottom, i)
			}
		}
	}
	return (right - left + 1) * (bottom - top + 1)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return minimumArea(grid)
}
