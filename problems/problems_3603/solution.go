package problem3603

import (
	"encoding/json"
	"log"
	"strings"
)

func minCost(m int, n int, waitCost [][]int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var m int
	var n int
	var waitCost [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &m); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &waitCost); err != nil {
		log.Fatal(err)
	}

	return minCost(m, n, waitCost)
}
