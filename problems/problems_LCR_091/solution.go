package problemLCR_091

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minCost(costs [][]int) (ans int) {
	dp := make([][]int, 2)
	for i := range dp {
		dp[i] = make([]int, 3)
	}
	for i, cost := range costs {
		pre, cur := i%2, (i+1)%2
		dp[cur][0] = cost[0] + min(dp[pre][1], dp[pre][2])
		dp[cur][1] = cost[1] + min(dp[pre][0], dp[pre][2])
		dp[cur][2] = cost[2] + min(dp[pre][0], dp[pre][1])
	}
	ans = math.MaxInt32
	for _, j := range dp[len(costs)%2] {
		ans = min(ans, j)
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var costs [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &costs); err != nil {
		log.Fatal(err)
	}

	return minCost(costs)
}
