package problem1140

import (
	"encoding/json"
	"log"
	"strings"
)

func stoneGameII(piles []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var piles []int

	if err := json.Unmarshal([]byte(inputValues[0]), &piles); err != nil {
		log.Fatal(err)
	}

	return stoneGameII(piles)
}
