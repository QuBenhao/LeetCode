package problem3373

import (
	"encoding/json"
	"log"
	"strings"
)

func maxTargetNodes(edges1 [][]int, edges2 [][]int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges1 [][]int
	var edges2 [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &edges1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges2); err != nil {
		log.Fatal(err)
	}

	return maxTargetNodes(edges1, edges2)
}
