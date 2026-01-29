package problem2977

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumCost(source string, target string, original []string, changed []string, cost []int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var source string
	var target string
	var original []string
	var changed []string
	var cost []int

	if err := json.Unmarshal([]byte(inputValues[0]), &source); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &original); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &changed); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[4]), &cost); err != nil {
		log.Fatal(err)
	}

	return minimumCost(source, target, original, changed, cost)
}
