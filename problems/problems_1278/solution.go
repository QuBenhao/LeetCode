package problem1278

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func palindromePartition(s string, k int) int {
	n := len(s)
	minChange := make([][]int, n)
	for i := n - 1; i >= 0; i-- {
		minChange[i] = make([]int, n)
		for j := i + 1; j < n; j++ {
			minChange[i][j] = minChange[i+1][j-1]
			if s[i] != s[j] {
				minChange[i][j]++
			}
		}
	}
	// Reduce the problem to enumerating right endpoints and minimizing the required changes
	dp := minChange[0]
	for i := 1; i < k; i++ {
		// The left side must allow i-1 cuts, so the right endpoint is at least i; k-1 cuts are required in total, so endpoints beyond n-k+i are unused
		// When reusing the dp array, update in reverse order because each state depends on values to its left
		for r := n - k + i; r >= i; r-- {
			dp[r] = math.MaxInt / 2
			for l := i; l <= r; l++ {
				dp[r] = min(dp[r], dp[l-1]+minChange[l][r])
			}
		}
	}
	return dp[n-1]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return palindromePartition(s, k)
}
