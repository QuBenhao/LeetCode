package problem1541

import (
	"encoding/json"
	"log"
	"strings"
)

func minInsertions(s string) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return minInsertions(s)
}
