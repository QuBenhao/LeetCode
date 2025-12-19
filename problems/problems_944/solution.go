package problem944

import (
	"encoding/json"
	"log"
	"strings"
)

func minDeletionSize(strs []string) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var strs []string

	if err := json.Unmarshal([]byte(inputValues[0]), &strs); err != nil {
		log.Fatal(err)
	}

	return minDeletionSize(strs)
}
