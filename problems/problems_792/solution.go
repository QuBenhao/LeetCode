package problem792

import (
	"encoding/json"
	"log"
	"strings"
)

func numMatchingSubseq(s string, words []string) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var words []string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &words); err != nil {
		log.Fatal(err)
	}

	return numMatchingSubseq(s, words)
}
