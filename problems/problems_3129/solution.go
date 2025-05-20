package problem3129

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfStableArrays(zero int, one int, limit int) int {
	const mod = 1_000_000_007
	dp := make([][][2]int, zero+1)
	for i := range dp {
		dp[i] = make([][2]int, one+1)
	}
	for i := 1; i <= min(zero, limit); i++ {
		dp[i][0][0] = 1
	}
	for j := 1; j <= min(one, limit); j++ {
		dp[0][j][1] = 1
	}
	for i := 1; i <= zero; i++ {
		for j := 1; j <= one; j++ {
			dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % mod
			if i > limit {
				dp[i][j][0] = (dp[i][j][0] - dp[i-limit-1][j][1] + mod) % mod
			}
			dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1]) % mod
			if j > limit {
				dp[i][j][1] = (dp[i][j][1] - dp[i][j-limit-1][0] + mod) % mod
			}
		}
	}
	return (dp[zero][one][0] + dp[zero][one][1]) % mod
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var zero int
	var one int
	var limit int

	if err := json.Unmarshal([]byte(inputValues[0]), &zero); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &one); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &limit); err != nil {
		log.Fatal(err)
	}

	return numberOfStableArrays(zero, one, limit)
}
