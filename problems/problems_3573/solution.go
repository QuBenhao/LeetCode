package problem3573

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumProfit(prices []int, k int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var prices []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &prices); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maximumProfit(prices, k)
}
