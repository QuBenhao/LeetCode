package problem2011

import (
	"encoding/json"
	"log"
	"strings"
)

func finalValueAfterOperations(operations []string) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var operations []string

	if err := json.Unmarshal([]byte(inputValues[0]), &operations); err != nil {
		log.Fatal(err)
	}

	return finalValueAfterOperations(operations)
}
