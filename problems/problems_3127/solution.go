package problem3127

import (
	"encoding/json"
	"log"
	"strings"
)

func canMakeSquare(grid [][]byte) bool {
	for m, n, i := len(grid), len(grid[0]), 0; i < m-1; i++ {
		for j := 0; j < n-1; j++ {
			count := 0
			for r := i; r < i+2; r++ {
				for c := j; c < j+2; c++ {
					if grid[r][c] == 'B' {
						count++
					}
				}
			}
			if count != 2 {
				return true
			}
		}
	}
	return false
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]byte

	var gridStr [][]string
	if err := json.Unmarshal([]byte(inputValues[0]), &gridStr); err != nil {
		log.Fatal(err)
	}
	grid = make([][]byte, len(gridStr))
	for i := 0; i < len(grid); i++ {
		grid[i] = make([]byte, len(gridStr[i]))
		for j := 0; j < len(grid[i]); j++ {
			grid[i][j] = gridStr[i][j][0]
		}
	}

	return canMakeSquare(grid)
}
