package problem3093

import (
	"encoding/json"
	"log"
	"strings"
)

func stringIndices(wordsContainer []string, wordsQuery []string) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var wordsContainer []string
	var wordsQuery []string

	if err := json.Unmarshal([]byte(inputValues[0]), &wordsContainer); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &wordsQuery); err != nil {
		log.Fatal(err)
	}

	return stringIndices(wordsContainer, wordsQuery)
}
