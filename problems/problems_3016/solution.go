package problem3016

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumPushes(word string) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var word string

	if err := json.Unmarshal([]byte(inputValues[0]), &word); err != nil {
		log.Fatal(err)
	}

	return minimumPushes(word)
}
