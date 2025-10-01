package problem3100

import (
	"encoding/json"
	"log"
	"strings"
)

func maxBottlesDrunk(numBottles int, numExchange int) int {
    
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

	return maxBottlesDrunk(numBottles, numExchange)
}
