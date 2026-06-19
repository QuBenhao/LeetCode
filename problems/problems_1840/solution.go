package problem1840

import (
	"encoding/json"
	"log"
	"strings"
)

func maxBuilding(n int, restrictions [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var restrictions [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &restrictions); err != nil {
		log.Fatal(err)
	}

	return maxBuilding(n, restrictions)
}
