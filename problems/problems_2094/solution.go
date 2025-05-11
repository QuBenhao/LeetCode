package problem2094

import (
	"encoding/json"
	"log"
	"strings"
)

func findEvenNumbers(digits []int) []int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var digits []int

	if err := json.Unmarshal([]byte(inputValues[0]), &digits); err != nil {
		log.Fatal(err)
	}

	return findEvenNumbers(digits)
}
