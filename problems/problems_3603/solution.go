package problem3603

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minCost(m int, n int, waitCost [][]int) int64 {
	dp := make([][]int64, m)
	for i := range dp {
		dp[i] = make([]int64, n)
		for j := range dp[i] {
			dp[i][j] = math.MaxInt64
		}
	}
	dp[0][0] = 1
	for i := range m {
		for j := range n {
			if i < m-1 {
				dp[i+1][j] = min(dp[i+1][j], dp[i][j]+int64(i+2)*int64(j+1)+int64(waitCost[i+1][j]))
			}
			if j < n-1 {
				dp[i][j+1] = min(dp[i][j+1], dp[i][j]+int64(i+1)*int64(j+2)+int64(waitCost[i][j+1]))
			}
		}
	}
	return dp[m-1][n-1] - int64(waitCost[m-1][n-1])
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var m int
	var n int
	var waitCost [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &m); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &waitCost); err != nil {
		log.Fatal(err)
	}

	return minCost(m, n, waitCost)
}
