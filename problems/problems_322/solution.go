package problem322

import (
	"encoding/json"
	"log"
	"strings"
)

func coinChange(coins []int, amount int) int {
	if amount == 0 {
		return 0
	}
	dp := make([]int, amount+1)
	for i := 1; i <= amount; i++ {
		dp[i] = 1<<31 - 1
		for _, coin := range coins {
			if i >= coin {
				dp[i] = min(dp[i], dp[i-coin]+1)
			}
		}
	}
	if dp[amount] == 1<<31-1 {
		return -1
	}
	return dp[amount]
}

func Solve(inputJsonValues string) interface{} {
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
