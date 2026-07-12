package problem1291

import (
	"encoding/json"
	"log"
	"strings"
)

func sequentialDigits(low int, high int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var low int
	var high int

	if err := json.Unmarshal([]byte(inputValues[0]), &low); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &high); err != nil {
		log.Fatal(err)
	}

	return sequentialDigits(low, high)
}
