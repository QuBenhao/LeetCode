package problem2707

import (
	"encoding/json"
	"log"
	"strings"
)

func minExtraChar(s string, dictionary []string) int {
	d := make(map[string]bool, len(dictionary))
	for _, word := range dictionary {
		d[word] = true
	}
	n := len(s)
	dp := make([]int, n+1)
	for i := 0; i < n; i++ {
		dp[i+1] = dp[i] + 1 // assume the next character is an extra character
		for j := 0; j <= i; j++ {
			if d[s[j:i+1]] {
				// if the substring s[j:i+1] is in the dictionary, then we can remove it
				dp[i+1] = min(dp[i+1], dp[j])
			}
		}
	}
	return dp[n]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var dictionary []string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &dictionary); err != nil {
		log.Fatal(err)
	}

	return minExtraChar(s, dictionary)
}
