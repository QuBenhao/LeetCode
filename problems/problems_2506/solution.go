package problem2506

import (
	"encoding/json"
	"log"
	"strings"
)

func similarPairs(words []string) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}

	return similarPairs(words)
}
