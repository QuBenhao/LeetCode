package problem3838

import (
	"encoding/json"
	"log"
	"strings"
)

func mapWordWeights(words []string, weights []int) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string
	var weights []int

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &weights); err != nil {
		log.Fatal(err)
	}

	return mapWordWeights(words, weights)
}
