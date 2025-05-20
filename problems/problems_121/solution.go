package problem121

import (
	"encoding/json"
	"log"
	"strings"
)

func maxProfit(prices []int) int {
	buy, sell := -prices[0], 0
	for i := 1; i < len(prices); i++ {
		buy = max(buy, -prices[i])
		sell = max(sell, buy+prices[i])
	}
	return sell
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var prices []int

	if err := json.Unmarshal([]byte(inputValues[0]), &prices); err != nil {
		log.Fatal(err)
	}

	return maxProfit(prices)
}
