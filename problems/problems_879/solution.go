package problem879

import (
	"encoding/json"
	"log"
	"strings"
)

const mod = 1_000_000_007

func profitableSchemes(n int, minProfit int, group []int, profit []int) (ans int) {
	if minProfit == 0 {
		ans++
	}
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, minProfit+1)
	}
	dp[0][0] = 1
	for i, g := range group {
		p := profit[i]
		for j := n; j >= g; j-- {
			for k := minProfit; k >= 0; k-- {
				newProfit := min(minProfit, k+p)
				dp[j][newProfit] = (dp[j][newProfit] + dp[j-g][k]) % mod
				if newProfit == minProfit {
					ans = (ans + dp[j-g][k]) % mod
				}
			}
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var minProfit int
	var group []int
	var profit []int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &minProfit); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &group); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &profit); err != nil {
		log.Fatal(err)
	}

	return profitableSchemes(n, minProfit, group, profit)
}
