package problem3128

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfRightTriangles(grid [][]int) (ans int64) {
	m, n := len(grid), len(grid[0])
	rowCount := make([]int, m)
	colCount := make([]int, n)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			rowCount[i] += grid[i][j]
			colCount[j] += grid[i][j]
		}
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				ans += int64(rowCount[i]-1) * int64(colCount[j]-1)
			}
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return numberOfRightTriangles(grid)
}
