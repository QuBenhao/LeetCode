package problem2266

import (
	"encoding/json"
	"log"
	"strings"
)

const MOD = 1000_000_007

var POSSIBILITIES = map[byte]int{'2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 4, '8': 3, '9': 4}

func countTexts(pressedKeys string) int {
	n := len(pressedKeys)
	dp := make([]int, n+1)
	dp[0] = 1
	for i := range n {
		dp[i+1] = dp[i]
		for j := i - 1; j >= 0 && i-j < POSSIBILITIES[pressedKeys[i]]; j-- {
			if pressedKeys[i] != pressedKeys[j] {
				break
			}
			dp[i+1] = (dp[i+1] + dp[j]) % MOD
		}
	}
	return dp[n]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var pressedKeys string

	if err := json.Unmarshal([]byte(inputValues[0]), &pressedKeys); err != nil {
		log.Fatal(err)
	}

	return countTexts(pressedKeys)
}
