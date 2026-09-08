package problem3871

import (
	"encoding/json"
	"log"
	"strings"
)

func countCommas(n int64) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int64

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return countCommas(n)
}
