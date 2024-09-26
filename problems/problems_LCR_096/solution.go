package problemLCR_096

import (
	"encoding/json"
	"log"
	"strings"
)

func isInterleave(s1 string, s2 string, s3 string) bool {
	m, n := len(s1), len(s2)
	if m+n != len(s3) {
		return false
	}
	dp := make([][]bool, m+1)
	for i := range dp {
		dp[i] = make([]bool, n+1)
	}
	dp[0][0] = true
	for i := 1; i <= m && s1[i-1] == s3[i-1]; i++ {
		dp[i][0] = true
	}
	for i := 1; i <= n && s2[i-1] == s3[i-1]; i++ {
		dp[0][i] = true
	}
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			dp[i][j] = dp[i-1][j] && s1[i-1] == s3[i+j-1] || dp[i][j-1] && s2[j-1] == s3[i+j-1]
		}
	}
	return dp[m][n]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s1 string
	var s2 string
	var s3 string

	if err := json.Unmarshal([]byte(inputValues[0]), &s1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &s2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &s3); err != nil {
		log.Fatal(err)
	}

	return isInterleave(s1, s2, s3)
}
