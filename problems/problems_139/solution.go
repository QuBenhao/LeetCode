package problem139

import (
	"encoding/json"
	"log"
	"strings"
)

func wordBreak(s string, wordDict []string) bool {
	words := map[string]bool{}
	for _, word := range wordDict {
		words[word] = true
	}
	n := len(s)
	dp := make([]bool, n+1)
	dp[0] = true
	for i := 1; i <= n; i++ {
		for j := 0; j < i; j++ {
			if dp[j] && words[s[j:i]] {
				dp[i] = true
				break
			}
		}
	}
	return dp[n]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var wordDict []string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &wordDict); err != nil {
		log.Fatal(err)
	}

	return wordBreak(s, wordDict)
}
