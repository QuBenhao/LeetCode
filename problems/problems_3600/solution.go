package problem3600

import (
	"encoding/json"
	"log"
	"strings"
)

func maxStability(n int, edges [][]int, k int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var edges [][]int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return maxStability(n, edges, k)
}
