package problem3557

import (
	"encoding/json"
	"log"
	"strings"
)

func maxSubstrings(word string) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var word string

	if err := json.Unmarshal([]byte(inputValues[0]), &word); err != nil {
		log.Fatal(err)
	}

	return maxSubstrings(word)
}
