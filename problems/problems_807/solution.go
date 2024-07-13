package problem807

import (
	"encoding/json"
	"log"
	"strings"
)

func maxIncreaseKeepingSkyline(grid [][]int) (ans int) {
	n := len(grid)
	rowMax := make([]int, n)
	colMax := make([]int, n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			rowMax[i] = max(rowMax[i], grid[i][j])
			colMax[j] = max(colMax[j], grid[i][j])
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			ans += min(rowMax[i], colMax[j]) - grid[i][j]
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return maxIncreaseKeepingSkyline(grid)
}
