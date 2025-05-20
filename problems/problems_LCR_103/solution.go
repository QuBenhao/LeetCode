package problemLCR_103

import (
	"encoding/json"
	"log"
	"strings"
)

func coinChange(coins []int, amount int) int {
	dp := make([]int, amount+1)
	for i := range dp {
		dp[i] = amount + 1
	}
	dp[0] = 0
	for _, coin := range coins {
		for i := coin; i <= amount; i++ {
			dp[i] = min(dp[i], dp[i-coin]+1)
		}
	}
	if dp[amount] == amount+1 {
		return -1
	}
	return dp[amount]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var coins []int
	var amount int

	if err := json.Unmarshal([]byte(inputValues[0]), &coins); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &amount); err != nil {
		log.Fatal(err)
	}

	return coinChange(coins, amount)
}
