package problem2872

import (
	"encoding/json"
	"log"
	"strings"
)

func maxKDivisibleComponents(n int, edges [][]int, values []int, k int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var edges [][]int
	var values []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &values); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &k); err != nil {
		log.Fatal(err)
	}

	return maxKDivisibleComponents(n, edges, values, k)
}
