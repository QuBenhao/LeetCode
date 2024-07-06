package problem200

import (
	"encoding/json"
	"log"
	"strings"
)

func numIslands(grid [][]byte) int {
    
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

	return numIslands(grid)
}
