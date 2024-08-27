package problem3144

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumSubstringsInPartition(s string) int {
	n := len(s)
	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = n
	}
	dp[0] = 0
	for i := 0; i < n; i++ {
		counter := make(map[byte]int)
		maxCount := 0
		for j := i; j >= 0; j-- {
			counter[s[j]]++
			maxCount = max(maxCount, counter[s[j]])
			if maxCount*len(counter) == i-j+1 {
				dp[i+1] = min(dp[i+1], dp[j]+1)
			}
		}
	}
	return dp[n]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return minimumSubstringsInPartition(s)
}
