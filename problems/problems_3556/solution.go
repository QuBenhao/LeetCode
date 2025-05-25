package problem3556

import (
	"encoding/json"
	"log"
	"strings"
)

func sumOfLargestPrimes(s string) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return sumOfLargestPrimes(s)
}
