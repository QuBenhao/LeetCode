package problem3593

import (
	"encoding/json"
	"log"
	"strings"
)

func minIncrease(n int, edges [][]int, cost []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var edges [][]int
	var cost []int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &cost); err != nil {
		log.Fatal(err)
	}

	return minIncrease(n, edges, cost)
}
