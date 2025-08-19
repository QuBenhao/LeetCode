package problem1277

import (
	"encoding/json"
	"log"
	"strings"
)

func countSquares(matrix [][]int) (ans int) {
	m, n := len(matrix), len(matrix[0])
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}
	for i, row := range matrix {
		for j, val := range row {
			if val == 1 {
				dp[i+1][j+1] = min(min(dp[i][j+1], dp[i+1][j]), dp[i][j]) + 1
				ans += dp[i+1][j+1]
			}
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var matrix [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &matrix); err != nil {
		log.Fatal(err)
	}

	return countSquares(matrix)
}
