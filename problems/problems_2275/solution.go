package problem2275

import (
	"encoding/json"
	"log"
	"strings"
)

func largestCombination(candidates []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var candidates []int

	if err := json.Unmarshal([]byte(inputValues[0]), &candidates); err != nil {
		log.Fatal(err)
	}

	return largestCombination(candidates)
}
