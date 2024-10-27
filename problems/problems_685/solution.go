package problem685

import (
	"encoding/json"
	"log"
	"strings"
)

func findRedundantDirectedConnection(edges [][]int) []int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &edges); err != nil {
		log.Fatal(err)
	}

	return findRedundantDirectedConnection(edges)
}
