package problem983

import (
	"encoding/json"
	"log"
	"strings"
)

func mincostTickets(days []int, costs []int) int {
	dp := make([]int, len(days)+1)
	j, k := 0, 0
	for i, d := range days {
		for days[j] <= d-7 {
			j += 1
		}
		for days[k] <= d-30 {
			k += 1
		}
		dp[i+1] = min(dp[j]+costs[1], dp[k]+costs[2], dp[i]+costs[0])
	}
	return dp[len(days)]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var days []int
	var costs []int

	if err := json.Unmarshal([]byte(inputValues[0]), &days); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &costs); err != nil {
		log.Fatal(err)
	}

	return mincostTickets(days, costs)
}
