package problem1547

import (
	"encoding/json"
	"log"
	"math"
	"sort"
	"strings"
)

func minCost(n int, cuts []int) int {
	cp := make([]int, len(cuts)+2)
	copy(cp, cuts)
	cp[len(cuts)] = 0
	cp[len(cuts)+1] = n
	sort.Ints(cp)
	m := len(cp)
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, m)
	}
	for i := m - 2; i >= 0; i-- {
		for j := i + 2; j < m; j++ {
			dp[i][j] = math.MaxInt
			for k := i + 1; k < j; k++ {
				dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
			}
			dp[i][j] += cp[j] - cp[i]
		}
	}
	return dp[0][m-1]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var cuts []int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &cuts); err != nil {
		log.Fatal(err)
	}

	return minCost(n, cuts)
}
