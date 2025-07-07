package problem1751

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func maxValue(events [][]int, k int) int {
	slices.SortFunc(events, func(a, b []int) int { return a[1] - b[1] })
	n := len(events)
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, k+1)
	}
	for i, event := range events {
		p, _ := slices.BinarySearchFunc(events, event[0], func(a []int, b int) int { return a[1] - b })
		for j := range k {
			dp[i+1][j+1] = max(dp[i][j+1], dp[p][j]+event[2])
		}
	}
	return dp[n][k]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var events [][]int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &events); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maxValue(events, k)
}
