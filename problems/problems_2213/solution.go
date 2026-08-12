package problem2213

import (
	"encoding/json"
	"log"
	"strings"
)

func longestRepeating(s string, queryCharacters string, queryIndices []int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var queryCharacters string
	var queryIndices []int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queryCharacters); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &queryIndices); err != nil {
		log.Fatal(err)
	}

	return longestRepeating(s, queryCharacters, queryIndices)
}
