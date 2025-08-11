package problem2787

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

const MOD = 1e9 + 7

func numberOfWays(n int, x int) int {
	dp := make([]int, n+1)
	dp[0] = 1
	for i := 1; i <= n; i++ {
		v := math.Pow(float64(i), float64(x))
		if v > float64(n) {
			break
		}
		for j := n; j >= int(v); j-- {
			dp[j] = (dp[j] + dp[j-int(v)]) % MOD
		}
	}
	return dp[n]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var x int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &x); err != nil {
		log.Fatal(err)
	}

	return numberOfWays(n, x)
}
