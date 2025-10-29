package problem1526

import (
	"encoding/json"
	"log"
	"strings"
)

func minNumberOperations(target []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var target []int

	if err := json.Unmarshal([]byte(inputValues[0]), &target); err != nil {
		log.Fatal(err)
	}

	return minNumberOperations(target)
}
