package problem1559

import (
	"encoding/json"
	"log"
	"strings"
)

func containsCycle(grid [][]byte) bool {
    
}

func Solve(inputJsonValues string) any {
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

	return containsCycle(grid)
}

func byteArrToStrArr(arr [][]byte) []string {
	ans := make([]string, len(arr))
	for i, b := range arr {
		ans[i] = string(b)
	}
	return ans
}
