package problem1463

import (
	"encoding/json"
	"log"
	"strings"
)

func cherryPickup(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	pre := make([][]int, n+2)
	cur := make([][]int, n+2)
	for i := range pre {
		pre[i] = make([]int, n+2)
		cur[i] = make([]int, n+2)
	}
	for i := m - 1; i >= 0; i-- {
		for j := 0; j < min(n, i+1); j++ {
			for k := max(j+1, n-1-i); k < n; k++ {
				cur[j+1][k+1] = max(
					pre[j][k], pre[j][k+1], pre[j][k+2],
					pre[j+1][k], pre[j+1][k+1], pre[j+1][k+2],
					pre[j+2][k], pre[j+2][k+1], pre[j+2][k+2],
				) + grid[i][j] + grid[i][k]
			}
		}
		pre, cur = cur, pre // 下一个 i 的 pre 是 cur
	}
	return pre[1][n]
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(values[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return cherryPickup(grid)
}
