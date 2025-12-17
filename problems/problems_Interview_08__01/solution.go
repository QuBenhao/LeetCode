package problemInterview_08__01

import (
	"encoding/json"
	"log"
	"strings"
)

const MOD = 1e9 + 7

func waysToStep(n int) int {
	dp := []int{1, 2, 4, 0}
	for i := 3; i < n; i++ {
		dp[i%4] = ((dp[(i+1)%4]+dp[(i+2)%4])%MOD + dp[(i+3)%4]) % MOD
	}
	return dp[(n+3)%4]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return waysToStep(n)
}
