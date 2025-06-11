package problem2767

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumBeautifulSubstrings(s string) int {
	isFivePow := func(num int) bool {
		if num == 0 {
			return false
		}
		for num > 1 {
			if num%5 != 0 {
				return false
			}
			num /= 5
		}
		return true
	}
	n := len(s)
	preSum := make([]int, n+1)
	for i := range n {
		preSum[i+1] = (preSum[i] << 1) + int(s[i]-'0')
	}
	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = n + 1
	}
	dp[0] = 0
	for i := range n {
		for j := range i + 1 {
			if s[j] == '0' {
				continue
			}
			if cur := preSum[i+1] ^ (preSum[j] << (i - j + 1)); isFivePow(cur) {
				dp[i+1] = min(dp[i+1], dp[j]+1)
			}
		}
	}
	if dp[n] == n+1 {
		return -1
	}
	return dp[n]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return minimumBeautifulSubstrings(s)
}
