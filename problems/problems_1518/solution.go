package problem1518

import (
	"encoding/json"
	"log"
	"strings"
)

func numWaterBottles(numBottles int, numExchange int) int {
	return numBottles + (numBottles-1)/(numExchange-1)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var numBottles int
	var numExchange int

	if err := json.Unmarshal([]byte(inputValues[0]), &numBottles); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &numExchange); err != nil {
		log.Fatal(err)
	}

	return numWaterBottles(numBottles, numExchange)
}
