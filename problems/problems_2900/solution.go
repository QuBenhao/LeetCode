package problem2900

import (
	"encoding/json"
	"log"
	"strings"
)

func getLongestSubsequence(words []string, groups []int) []string {
	var dp0, dp1 []string
	for i, word := range words {
		if len(dp0)%2 == groups[i] {
			dp0 = append(dp0, word)
		}
		if len(dp1)%2 == groups[i]^1 {
			dp1 = append(dp1, word)
		}
	}
	if len(dp0) > len(dp1) {
		return dp0
	} else {
		return dp1
	}
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string
	var groups []int

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &groups); err != nil {
		log.Fatal(err)
	}

	return getLongestSubsequence(words, groups)
}
