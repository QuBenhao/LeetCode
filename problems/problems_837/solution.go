package problem837

import (
	"encoding/json"
	"log"
	"strings"
)

func new21Game(n int, k int, maxPts int) float64 {
	dp := make([]float64, n+1)
	var s float64
	for i := n; i >= 0; i-- {
		if i >= k {
			dp[i] = 1
		} else {
			dp[i] = s / float64(maxPts)
		}
		s += dp[i]
		if i+maxPts <= n {
			s -= dp[i+maxPts]
		}
	}
	return dp[0]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var k int
	var maxPts int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &maxPts); err != nil {
		log.Fatal(err)
	}

	return new21Game(n, k, maxPts)
}
