package problem3663

import (
	"encoding/json"
	"log"
	"strings"
)

func getLeastFrequentDigit(n int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return getLeastFrequentDigit(n)
}
