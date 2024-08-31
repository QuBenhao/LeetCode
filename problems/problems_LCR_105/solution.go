package problemLCR_105

import (
	"encoding/json"
	"log"
	"strings"
)

func maxAreaOfIsland(grid [][]int) (ans int) {
	m, n := len(grid), len(grid[0])
	dirs := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	var dfs func(int, int) int
	dfs = func(i, j int) int {
		if i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == 0 {
			return 0
		}
		grid[i][j] = 0
		res := 1
		for _, dir := range dirs {
			res += dfs(i+dir[0], j+dir[1])
		}
		return res
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				ans = max(ans, dfs(i, j))
			}
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

	return maxAreaOfIsland(grid)
}
