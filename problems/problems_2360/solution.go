package problem2360

import (
	"encoding/json"
	"log"
	"strings"
)

func longestCycle(edges []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges []int

	if err := json.Unmarshal([]byte(inputValues[0]), &edges); err != nil {
		log.Fatal(err)
	}

	return longestCycle(edges)
}
