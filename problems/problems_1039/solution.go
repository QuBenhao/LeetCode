package problem1039

import (
	"encoding/json"
	"log"
	"strings"
)

func minScoreTriangulation(values []int) int {
	n := len(values)
	dp := make([][]int, n)
	for i := range n {
		dp[i] = make([]int, n)
	}
	for len := 2; len < n; len++ {
		for i := 0; i < n-len; i++ {
			dp[i][i+len] = 0x3fffff
			for j, k := i+len, i+1; k < j; k++ {
				dp[i][j] = min(dp[i][j], values[i]*values[k]*values[j]+dp[i][k]+dp[k][j])
			}
		}
	}
	return dp[0][n-1]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var values []int

	if err := json.Unmarshal([]byte(inputValues[0]), &values); err != nil {
		log.Fatal(err)
	}

	return minScoreTriangulation(values)
}
