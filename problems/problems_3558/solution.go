package problem3558

import (
	"encoding/json"
	"log"
	"strings"
)

func assignEdgeWeights(edges [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &edges); err != nil {
		log.Fatal(err)
	}

	return assignEdgeWeights(edges)
}
