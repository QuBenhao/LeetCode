package problem1561

import (
	"encoding/json"
	"log"
	"strings"
)

func maxCoins(piles []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var piles []int

	if err := json.Unmarshal([]byte(inputValues[0]), &piles); err != nil {
		log.Fatal(err)
	}

	return maxCoins(piles)
}
