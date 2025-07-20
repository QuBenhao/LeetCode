package problem3619

import (
	"encoding/json"
	"log"
	"strings"
)

var DIRECTIONS = [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

func countIslands(grid [][]int, k int) (ans int) {
	m, n := len(grid), len(grid[0])
	visited := make([][]bool, m)
	for i := range visited {
		visited[i] = make([]bool, n)
	}

	var dfs func(int, int) int
	dfs = func(x, y int) (cur int) {
		cur = grid[x][y] % k
		for _, d := range DIRECTIONS {
			nx, ny := x+d[0], y+d[1]
			if nx < 0 || nx >= m || ny < 0 || ny >= n || visited[nx][ny] || grid[nx][ny] == 0 {
				continue
			}
			visited[nx][ny] = true
			cur = (cur + dfs(nx, ny)) % k
		}
		return
	}
	for i := range m {
		for j := range n {
			if visited[i][j] || grid[i][j] == 0 {
				continue
			}
			visited[i][j] = true
			if dfs(i, j) == 0 {
				ans++
			}
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return countIslands(grid, k)
}
