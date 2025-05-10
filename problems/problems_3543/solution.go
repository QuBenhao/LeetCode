package problem3543

import (
	"encoding/json"
	"log"
	"strings"
)

func maxWeight(n int, edges [][]int, k int, t int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var edges [][]int
	var k int
	var t int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &t); err != nil {
		log.Fatal(err)
	}

	return maxWeight(n, edges, k, t)
}
