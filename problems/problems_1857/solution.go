package problem1857

import (
	"encoding/json"
	"log"
	"strings"
)

func largestPathValue(colors string, edges [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var colors string
	var edges [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &colors); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges); err != nil {
		log.Fatal(err)
	}

	return largestPathValue(colors, edges)
}
