package problem2087

import (
	"encoding/json"
	"log"
	"strings"
)

func minCost(startPos []int, homePos []int, rowCosts []int, colCosts []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var startPos []int
	var homePos []int
	var rowCosts []int
	var colCosts []int

	if err := json.Unmarshal([]byte(inputValues[0]), &startPos); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &homePos); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &rowCosts); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &colCosts); err != nil {
		log.Fatal(err)
	}

	return minCost(startPos, homePos, rowCosts, colCosts)
}
