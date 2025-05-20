package problem2140

import (
	"encoding/json"
	"log"
	"strings"
)

func mostPoints(questions [][]int) int64 {
	n := len(questions)
	dp := make([]int64, n+1)
	for i, question := range questions {
		dp[i+1] = max(dp[i+1], dp[i])
		nxt := min(n, i+question[1]+1)
		dp[nxt] = max(dp[nxt], dp[i]+int64(question[0]))
	}
	return dp[n]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var questions [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &questions); err != nil {
		log.Fatal(err)
	}

	return mostPoints(questions)
}
