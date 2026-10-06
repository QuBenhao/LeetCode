package problem741

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func cherryPickup(grid [][]int) int {
	n := len(grid)
	memo := make([][][]int, n*2-1)
	for i := range memo {
		memo[i] = make([][]int, n)
		for j := range memo[i] {
			memo[i][j] = make([]int, n)
			for k := range memo[i][j] {
				memo[i][j][k] = -1 // -1 means not yet computed
			}
		}
	}
	var dfs func(int, int, int) int
	dfs = func(t, j, k int) int {
		// Stay within bounds and avoid cells containing -1
		if j < 0 || k < 0 || t < j || t < k || grid[t-j][j] < 0 || grid[t-k][k] < 0 {
			return math.MinInt
		}
		if t == 0 { // Here j = k = 0
			return grid[0][0]
		}
		p := &memo[t][j][k]
		if *p != -1 { // Already computed
			return *p
		}
		res := max(dfs(t-1, j, k), dfs(t-1, j, k-1), dfs(t-1, j-1, k), dfs(t-1, j-1, k-1)) + grid[t-j][j]
		if k != j {
			res += grid[t-k][k]
		}
		*p = res // Memoization
		return res
	}
	return max(dfs(n*2-2, n-1, n-1), 0)
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(values[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return cherryPickup(grid)
}
