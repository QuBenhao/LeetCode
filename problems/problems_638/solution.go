package problem638

import (
	"encoding/json"
	"log"
	"strings"
)

func shoppingOffers(price []int, special [][]int, needs []int) int {
	n := len(price)
	columns := make([]int, n+1)
	columns[0] = 1
	for i, need := range needs {
		// need + 1 because we need to consider the case where we don't buy any of this item
		columns[i+1] = columns[i] * (need + 1)
	}
	dp := make([]int, columns[n]+1)
	for i := 1; i <= columns[n]; i++ {
		curNeeds := make([]int, n)
		for j := 0; j < n; j++ {
			curNeeds[j] = (i % columns[j+1]) / columns[j]
		}
		for j, p := range price {
			dp[i] += curNeeds[j] * p
		}
		for _, offer := range special {
			prev := 0
			for j := 0; j < n; j++ {
				if curNeeds[j] < offer[j] {
					prev = -1
					break
				}
				prev += offer[j] * columns[j]
			}
			if prev == -1 {
				continue
			}
			dp[i] = min(dp[i], dp[i-prev]+offer[n])
		}
	}
	return dp[columns[n]-1]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var price []int
	var special [][]int
	var needs []int

	if err := json.Unmarshal([]byte(inputValues[0]), &price); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &special); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &needs); err != nil {
		log.Fatal(err)
	}

	return shoppingOffers(price, special, needs)
}
