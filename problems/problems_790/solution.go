package problem790

import (
	"encoding/json"
	"log"
	"strings"
)

const MOD = 1000000007

func numTilings(n int) int {
	dp := make([][]int, 2)
	for i := range 2 {
		dp[i] = make([]int, 4)
	}
	dp[1][0] = 1
	dp[1][3] = 1
	for i := 2; i <= n; i++ {
		cur, prev := i%2, (i+1)%2
		dp[cur][0] = dp[prev][3] % MOD
		dp[cur][1] = (dp[prev][0] + dp[prev][2]) % MOD
		dp[cur][2] = (dp[prev][0] + dp[prev][1]) % MOD
		dp[cur][3] = ((dp[cur][1]+dp[prev][1])%MOD + dp[prev][3]) % MOD
	}
	return dp[n%2][3] % MOD
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return numTilings(n)
}
