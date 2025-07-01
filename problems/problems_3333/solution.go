package problem3333

import (
	"encoding/json"
	"log"
	"strings"
)

const mod = 1000000007

func possibleStringCount(word string, k int) int {
	n := len(word)
	var ans int64
	ans = 1
	var groups []int
	for i := 0; i < n; {
		start := i
		for i < n && word[i] == word[start] {
			i++
		}
		k--
		if cur := i - start; cur > 1 {
			ans = ans * int64(cur) % mod
			groups = append(groups, cur-1)
		}
	}
	if k <= 0 {
		return int(ans)
	}
	dp := make([]int, k)
	for i := range dp {
		dp[i] = 1
	}
	for _, g := range groups {
		for i := 1; i < k; i++ {
			dp[i] = (dp[i] + dp[i-1]) % mod
		}
		for i := k - 1; i > g; i-- {
			dp[i] = (dp[i] - dp[i-g-1] + mod) % mod
		}
	}
	return int((ans - int64(dp[k-1]) + mod) % mod)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var word string
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &word); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return possibleStringCount(word, k)
}
