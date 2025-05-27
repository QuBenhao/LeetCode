package problem3372

import (
	"encoding/json"
	"log"
	"strings"
)

func maxTargetNodes(edges1 [][]int, edges2 [][]int, k int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges1 [][]int
	var edges2 [][]int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &edges1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return maxTargetNodes(edges1, edges2, k)
}
