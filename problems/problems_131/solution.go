package problem131

import (
	"encoding/json"
	"log"
	"strings"
)

func partition(s string) (ans [][]string) {
	n := len(s)
	dp := make([][]bool, n)
	for i := range dp {
		dp[i] = make([]bool, n)
		for j := range dp[i] {
			dp[i][j] = i == j
		}
	}
	for i := n - 1; i >= 0; i-- {
		for j := i; j < n; j++ {
			if s[i] == s[j] && (j-i <= 2 || dp[i+1][j-1]) {
				dp[i][j] = true
			}
		}
	}
	var path []string
	var backtrack func(int)
	backtrack = func(i int) {
		if i == n {
			ans = append(ans, append([]string(nil), path...))
			return
		}
		for j := i; j < n; j++ {
			if dp[i][j] {
				path = append(path, s[i:j+1])
				backtrack(j + 1)
				path = path[:len(path)-1]
			}
		}
	}
	backtrack(0)
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return partition(s)
}
