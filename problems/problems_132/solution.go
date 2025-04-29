package problem132

import (
	"encoding/json"
	"log"
	"strings"
)

func minCut(s string) int {
	n := len(s)
	isPalindrome := make([][]bool, n)
	for i := 0; i < n; i++ {
		isPalindrome[i] = make([]bool, n)
	}
	for i := 0; i < n; i++ {
		for j := i; j >= 0; j-- {
			if s[j] == s[i] && (i-j <= 1 || isPalindrome[j+1][i-1]) {
				isPalindrome[j][i] = true
			}
		}
	}
	dp := make([]int, n)
	for i := 1; i < n; i++ {
		dp[i] = i
		if isPalindrome[0][i] {
			dp[i] = 0
		} else {
			for j := 1; j <= i; j++ {
				if isPalindrome[j][i] {
					dp[i] = min(dp[i], dp[j-1]+1)
				}
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
