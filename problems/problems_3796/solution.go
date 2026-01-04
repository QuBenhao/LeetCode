package problem3796

import (
	"encoding/json"
	"log"
	"strings"
)

func findMaxVal(n int, restrictions [][]int, diff []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var restrictions [][]int
	var diff []int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &restrictions); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &diff); err != nil {
		log.Fatal(err)
	}

	return findMaxVal(n, restrictions, diff)
}
