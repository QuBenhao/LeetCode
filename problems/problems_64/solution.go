package problem64

import (
	"encoding/json"
	"log"
	"strings"
)

func minPathSum(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	dp := make([]int, n)
	for i := 0; i < m; i++ {
		dp[0] += grid[i][0]
		for j := 1; j < n; j++ {
			if i == 0 {
				dp[j] = dp[j-1] + grid[i][j]
			} else {
				dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
			}
		}
	}
	return dp[n-1]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return minPathSum(grid)
}
