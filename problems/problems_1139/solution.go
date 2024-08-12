package problem1139

import (
	"encoding/json"
	"log"
	"strings"
)

func largest1BorderedSquare(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	preRow := make([][]int, m)
	preCol := make([][]int, n)
	for i := 0; i < m; i++ {
		preRow[i] = make([]int, n+1)
	}
	for i := 0; i < n; i++ {
		preCol[i] = make([]int, m+1)
	}
	for i, row := range grid {
		for j, cell := range row {
			preRow[i][j+1] = preRow[i][j] + cell
			preCol[j][i+1] = preCol[j][i] + cell
		}
	}
	for d := min(m, n); d > 0; d-- {
		for i := 0; i+d <= m; i++ {
			for j := 0; j+d <= n; j++ {
				if preRow[i][j+d]-preRow[i][j] == d && preRow[i+d-1][j+d]-preRow[i+d-1][j] == d &&
					preCol[j][i+d]-preCol[j][i] == d && preCol[j+d-1][i+d]-preCol[j+d-1][i] == d {
					return d * d
				}
			}
		}
	}
	return 0
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return largest1BorderedSquare(grid)
}
