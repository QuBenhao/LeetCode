package problem2056

import (
	"encoding/json"
	"log"
	"strings"
)

func countCombinations(pieces []string, positions [][]int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var pieces []string
	var positions [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &pieces); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &positions); err != nil {
		log.Fatal(err)
	}

	return countCombinations(pieces, positions)
}
