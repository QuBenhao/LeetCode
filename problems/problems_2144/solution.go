package problem2144

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumCost(cost []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var cost []int

	if err := json.Unmarshal([]byte(inputValues[0]), &cost); err != nil {
		log.Fatal(err)
	}

	return minimumCost(cost)
}
