package problem3784

import (
	"encoding/json"
	"log"
	"strings"
)

func minCost(s string, cost []int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var cost []int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &cost); err != nil {
		log.Fatal(err)
	}

	return minCost(s, cost)
}
