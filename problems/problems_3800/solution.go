package problem3800

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumCost(s string, t string, flipCost int, swapCost int, crossCost int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var t string
	var flipCost int
	var swapCost int
	var crossCost int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &t); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &flipCost); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &swapCost); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[4]), &crossCost); err != nil {
		log.Fatal(err)
	}

	return minimumCost(s, t, flipCost, swapCost, crossCost)
}
