package problem3805

import (
	"encoding/json"
	"log"
	"strings"
)

func countPairs(words []string) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}

	return countPairs(words)
}
