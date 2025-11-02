package problem1578

import (
	"encoding/json"
	"log"
	"strings"
)

func minCost(colors string, neededTime []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var colors string
	var neededTime []int

	if err := json.Unmarshal([]byte(inputValues[0]), &colors); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &neededTime); err != nil {
		log.Fatal(err)
	}

	return minCost(colors, neededTime)
}
