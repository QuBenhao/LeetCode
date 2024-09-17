package problemLCR_094

import (
	"encoding/json"
	"log"
	"strings"
)

func minCut(s string) int {
	n := len(s)
	if n == 0 {
		return 0
	}

	isPalindrome := make([][]bool, n)
	for i := range isPalindrome {
		isPalindrome[i] = make([]bool, n)
	}

	for i := n - 1; i >= 0; i-- {
		for j := i; j < n; j++ {
			if s[i] == s[j] && (j-i < 2 || isPalindrome[i+1][j-1]) {
				isPalindrome[i][j] = true
			}
		}
	}

	dp := make([]int, n)
	for i := range dp {
		dp[i] = i
	}

	for i := 0; i < n; i++ {
		if isPalindrome[0][i] {
			dp[i] = 0
			continue
		}

		for j := 0; j < i; j++ {
			if isPalindrome[j+1][i] {
				dp[i] = min(dp[i], dp[j]+1)
			}
		}
	}

	return dp[n-1]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return minCut(s)
}
