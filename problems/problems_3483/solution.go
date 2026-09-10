package problem3483

import (
	"encoding/json"
	"log"
	"strings"
)

func totalNumbers(digits []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var digits []int

	if err := json.Unmarshal([]byte(inputValues[0]), &digits); err != nil {
		log.Fatal(err)
	}

	return totalNumbers(digits)
}
