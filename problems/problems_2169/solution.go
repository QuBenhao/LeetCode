package problem2169

import (
	"encoding/json"
	"log"
	"strings"
)

func countOperations(num1 int, num2 int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num1 int
	var num2 int

	if err := json.Unmarshal([]byte(inputValues[0]), &num1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &num2); err != nil {
		log.Fatal(err)
	}

	return countOperations(num1, num2)
}
