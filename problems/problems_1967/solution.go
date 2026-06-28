package problem1967

import (
	"encoding/json"
	"log"
	"strings"
)

func numOfStrings(patterns []string, word string) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var patterns []string
	var word string

	if err := json.Unmarshal([]byte(inputValues[0]), &patterns); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &word); err != nil {
		log.Fatal(err)
	}

	return numOfStrings(patterns, word)
}
