package problem1547

import (
	"encoding/json"
	"log"
	"strings"
)

func minCost(n int, cuts []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var cuts []int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &cuts); err != nil {
		log.Fatal(err)
	}

	return minCost(n, cuts)
}
