package problem3577

import (
	"encoding/json"
	"log"
	"strings"
)

func countPermutations(complexity []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var complexity []int

	if err := json.Unmarshal([]byte(inputValues[0]), &complexity); err != nil {
		log.Fatal(err)
	}

	return countPermutations(complexity)
}
