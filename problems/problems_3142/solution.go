package problem3142

import (
	"encoding/json"
	"log"
	"strings"
)

func satisfiesConditions(grid [][]int) bool {
	for j := 0; j < len(grid[0])-1; j++ {
		if grid[0][j] == grid[0][j+1] {
			return false
		}
	}
	for i := 0; i < len(grid)-1; i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] != grid[i+1][j] {
				return false
			}
		}
	}
	return true
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return satisfiesConditions(grid)
}
