package problem2515

import (
	"encoding/json"
	"log"
	"strings"
)

func closestTarget(words []string, target string, startIndex int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string
	var target string
	var startIndex int

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &startIndex); err != nil {
		log.Fatal(err)
	}

	return closestTarget(words, target, startIndex)
}
