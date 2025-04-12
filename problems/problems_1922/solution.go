package problem1922

import (
	"encoding/json"
	"log"
	"strings"
)

func countGoodNumbers(n int64) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int64

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return countGoodNumbers(n)
}
