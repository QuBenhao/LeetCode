package problem3786

import (
	"encoding/json"
	"log"
	"strings"
)

func interactionCosts(n int, edges [][]int, group []int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var edges [][]int
	var group []int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &group); err != nil {
		log.Fatal(err)
	}

	return interactionCosts(n, edges, group)
}
