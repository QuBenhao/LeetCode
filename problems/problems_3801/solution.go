package problem3801

import (
	"encoding/json"
	"log"
	"strings"
)

func minMergeCost(lists [][]int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var lists [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &lists); err != nil {
		log.Fatal(err)
	}

	return minMergeCost(lists)
}
