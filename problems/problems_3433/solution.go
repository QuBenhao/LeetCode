package problem3433

import (
	"encoding/json"
	"log"
	"strings"
)

func countMentions(numberOfUsers int, events [][]string) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var numberOfUsers int
	var events [][]string

	if err := json.Unmarshal([]byte(inputValues[0]), &numberOfUsers); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &events); err != nil {
		log.Fatal(err)
	}

	return countMentions(numberOfUsers, events)
}
