package problem2561

import (
	"encoding/json"
	"log"
	"strings"
)

func minCost(basket1 []int, basket2 []int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var basket1 []int
	var basket2 []int

	if err := json.Unmarshal([]byte(inputValues[0]), &basket1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &basket2); err != nil {
		log.Fatal(err)
	}

	return minCost(basket1, basket2)
}
