package problem200

import (
	"encoding/json"
	"log"
	"strings"
)

func numIslands(grid [][]byte) (ans int) {
	m, n := len(grid), len(grid[0])
	directions := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	var dfs func(i, j int)
	dfs = func(i, j int) {
		if i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0' {
			return
		}
		grid[i][j] = '0'
		for _, d := range directions {
			dfs(i+d[0], j+d[1])
		}
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == '1' {
				ans++
				dfs(i, j)
			}
		}
	}
	return
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

	return numIslands(grid)
}
